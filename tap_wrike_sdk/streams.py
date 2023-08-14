"""Stream type classes for tap-wrike-sdk."""

from __future__ import annotations

from pathlib import Path

from singer_sdk import typing as th  # JSON Schema typing helpers

from tap_wrike_sdk.client import wrikeStream

from tap_wrike_sdk.schemas import (
    Timelogs,
    Tasks,
)


class TimelogsStream(wrikeStream):
    name = "timelogs"
    path = "/v4/timelogs"
    primary_keys = ["id"]
    records_jsonpath = "$.data[*]"
    replication_method = "INCREMENTAL"
    replication_key = "updatedDate"
    schema = Timelogs.schema

    def get_url_params(
        self, context: Optional[dict], next_page_token: Optional[Any]
    ) -> Dict[str, Any]:
        params: dict = {}
        params["fields"] = '[\"billingType\"]'
        return params

class TasksStream(wrikeStream):
    name = "tasks"
    path = "/v4/tasks"
    primary_keys = ["id"]
    records_jsonpath = "$.data[*]"
    replication_method = "INCREMENTAL"
    replication_key = "updatedDate"
    schema = Tasks.schema

    def get_url_params(
        self, context: Optional[dict], next_page_token: Optional[Any]
    ) -> Dict[str, Any]:
        params: dict = {}
        params["fields"] = "[\"authorIds\",\"hasAttachments\",\"attachmentCount\",\"parentIds\",\"superParentIds\",\"sharedIds\",\"responsibleIds\",\"responsiblePlaceholderIds\",\"description\",\"briefDescription\",\"recurrent\",\"superTaskIds\",\"subTaskIds\",\"dependencyIds\",\"metadata\",\"customFields\",\"effortAllocation\",\"billingType\"]"
        params["pageSize"] = 1000
        return params
