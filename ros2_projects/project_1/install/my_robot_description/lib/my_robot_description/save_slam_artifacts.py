#!/usr/bin/env python3

import os

from ament_index_python.packages import get_package_prefix
import rclpy
from rclpy.node import Node
from slam_toolbox.srv import SaveMap, SerializePoseGraph


class SaveSlamArtifactsNode(Node):
    def __init__(self):
        super().__init__("save_slam_artifacts")

        workspace_root = os.path.abspath(
            os.path.join(get_package_prefix("my_robot_description"), "..", "..")
        )
        default_maps_dir = os.path.join(
            workspace_root, "src", "my_robot_description", "maps"
        )

        self.declare_parameter("maps_dir", default_maps_dir)
        self.declare_parameter("map_basename", "learning_room_map")
        self.declare_parameter("posegraph_basename", "learning_room_posegraph")
        self.declare_parameter("save_map_service", "/slam_toolbox/save_map")
        self.declare_parameter("serialize_service", "/slam_toolbox/serialize_map")
        self.declare_parameter("wait_timeout_sec", 8.0)

        self.maps_dir = str(self.get_parameter("maps_dir").value)
        self.map_basename = str(self.get_parameter("map_basename").value)
        self.posegraph_basename = str(self.get_parameter("posegraph_basename").value)
        self.save_map_service_name = str(self.get_parameter("save_map_service").value)
        self.serialize_service_name = str(
            self.get_parameter("serialize_service").value
        )
        self.wait_timeout_sec = float(self.get_parameter("wait_timeout_sec").value)

        os.makedirs(self.maps_dir, exist_ok=True)

        self.save_map_client = self.create_client(
            SaveMap, self.save_map_service_name
        )
        self.serialize_client = self.create_client(
            SerializePoseGraph, self.serialize_service_name
        )

    def run(self):
        map_prefix = os.path.join(self.maps_dir, self.map_basename)
        posegraph_prefix = os.path.join(self.maps_dir, self.posegraph_basename)

        self.get_logger().info(
            "Saving SLAM artifacts: "
            f"map_prefix={map_prefix}, posegraph_prefix={posegraph_prefix}"
        )

        if not self.save_map_client.wait_for_service(timeout_sec=self.wait_timeout_sec):
            self.get_logger().error(
                f"Service unavailable: {self.save_map_service_name}"
            )
            return 1

        if not self.serialize_client.wait_for_service(
            timeout_sec=self.wait_timeout_sec
        ):
            self.get_logger().error(
                f"Service unavailable: {self.serialize_service_name}"
            )
            return 1

        save_map_request = SaveMap.Request()
        save_map_request.name.data = map_prefix
        save_map_future = self.save_map_client.call_async(save_map_request)
        rclpy.spin_until_future_complete(self, save_map_future)

        if not save_map_future.result():
            self.get_logger().error("save_map call failed with no response.")
            return 1

        save_map_response = save_map_future.result()
        self.get_logger().info(f"save_map result={save_map_response.result}")
        if save_map_response.result != SaveMap.Response.RESULT_SUCCESS:
            self.get_logger().error("save_map reported failure.")
            return 1

        serialize_request = SerializePoseGraph.Request()
        serialize_request.filename = posegraph_prefix
        serialize_future = self.serialize_client.call_async(serialize_request)
        rclpy.spin_until_future_complete(self, serialize_future)

        if not serialize_future.result():
            self.get_logger().error("serialize_map call failed with no response.")
            return 1

        serialize_response = serialize_future.result()
        self.get_logger().info(
            f"serialize_map result={serialize_response.result}"
        )
        if (
            serialize_response.result
            != SerializePoseGraph.Response.RESULT_SUCCESS
        ):
            self.get_logger().error("serialize_map reported failure.")
            return 1
        self.get_logger().info("SLAM artifacts saved successfully.")
        return 0


def main():
    rclpy.init()
    node = SaveSlamArtifactsNode()
    exit_code = 1
    try:
        exit_code = node.run()
    finally:
        node.destroy_node()
        rclpy.shutdown()
    raise SystemExit(exit_code)


if __name__ == "__main__":
    main()
