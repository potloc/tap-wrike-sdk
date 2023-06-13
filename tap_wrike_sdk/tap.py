"""wrike tap class."""

from __future__ import annotations

from singer_sdk import Tap
from singer_sdk import typing as th  # JSON schema typing helpers

# TODO: Import your custom stream types here:
from tap_wrike_sdk import streams


class Tapwrike(Tap):
    """wrike tap class."""

    name = "tap-wrike-sdk"

    # TODO: Update this section with the actual config values you expect:
    config_jsonschema = th.PropertiesList(
        # th.Property(
        #     "auth_token",
        #     th.StringType,
        #     required=True,
        #     secret=True,  # Flag config as protected.
        #     description="The token to authenticate against the API service",
        # ),
        # th.Property(
        #     "project_ids",
        #     th.ArrayType(th.StringType),
        #     required=True,
        #     description="Project IDs to replicate",
        # ),
        # th.Property(
        #     "start_date",
        #     th.DateTimeType,
        #     description="The earliest record date to sync",
        # ),
        th.Property(
            "api_url",
            th.StringType,
            default="https://www.wrike.com/api",
            description="The url for the API service",
        ),
        th.Property(
            "token",
            th.StringType,
            required=False,
            secret=True,
            description="Access Token",
        ),
        th.Property(
            "client_id",
            th.StringType,
            required=False,
            secret=False,
            description="Client ID for API call.",
        ),
        th.Property(
            "client_secret",
            th.StringType,
            required=False,
            secret=True,
            description="Client secret to provide for API calls",
        ),
        th.Property(
            "refresh_token",
            th.StringType,
            required=False,
            secret=True,
            description="Refresh token for OAuth",
        ),
        th.Property(
            "start_date",
            th.DateTimeType,
            description="The earliest record date to sync",
        ),
    ).to_dict()

    def discover_streams(self) -> list[streams.wrikeStream]:
        """Return a list of discovered streams.

        Returns:
            A list of discovered streams.
        """
        return [
            streams.TimelogsStream(self),
        ]


if __name__ == "__main__":
    Tapwrike.cli()
