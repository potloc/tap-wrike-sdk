"""Stream type classes for tap-wrike-sdk."""

from __future__ import annotations

from pathlib import Path

from singer_sdk import typing as th  # JSON Schema typing helpers

from tap_wrike_sdk.client import wrikeStream

from tap_wrike_sdk.schemas import (
    Timelogs,
)


class TimelogsStream(wrikeStream):
    _LOG_REQUEST_METRIC_URLS = True
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
