# SPDX-License-Identifier: Apache-2.0
# Copyright 2022 Atlan Pte. Ltd.
# Based on original code from https://github.com/apache/atlas (under Apache-2.0 license)


from __future__ import annotations

from typing import ClassVar, Optional

from pydantic import Field, validator

from pyatlan.model.enums import KafkaTopicCompressionType, PowerbiEndorsement
from pyatlan.model.structs import KafkaTopicConsumption

from .asset50 import Kafka


class KafkaConsumerGroup(Kafka):
    """Description"""

    type_name: str = Field("KafkaConsumerGroup", allow_mutation=False)

    @validator("type_name")
    def validate_type_name(cls, v):
        if v != "KafkaConsumerGroup":
            raise ValueError("must be KafkaConsumerGroup")
        return v

    def __setattr__(self, name, value):
        if name in KafkaConsumerGroup._convience_properties:
            return object.__setattr__(self, name, value)
        super().__setattr__(name, value)

    _convience_properties: ClassVar[list[str]] = [
        "kafka_consumer_group_topic_consumption_properties",
        "kafka_consumer_group_member_count",
        "kafka_topic_names",
        "kafka_topic_qualified_names",
        "kafka_topics",
    ]

    @property
    def kafka_consumer_group_topic_consumption_properties(
        self,
    ) -> Optional[list[KafkaTopicConsumption]]:
        return (
            None
            if self.attributes is None
            else self.attributes.kafka_consumer_group_topic_consumption_properties
        )

    @kafka_consumer_group_topic_consumption_properties.setter
    def kafka_consumer_group_topic_consumption_properties(
        self,
        kafka_consumer_group_topic_consumption_properties: Optional[
            list[KafkaTopicConsumption]
        ],
    ):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.kafka_consumer_group_topic_consumption_properties = (
            kafka_consumer_group_topic_consumption_properties
        )

    @property
    def kafka_consumer_group_member_count(self) -> Optional[int]:
        return (
            None
            if self.attributes is None
            else self.attributes.kafka_consumer_group_member_count
        )

    @kafka_consumer_group_member_count.setter
    def kafka_consumer_group_member_count(
        self, kafka_consumer_group_member_count: Optional[int]
    ):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.kafka_consumer_group_member_count = (
            kafka_consumer_group_member_count
        )

    @property
    def kafka_topic_names(self) -> Optional[set[str]]:
        return None if self.attributes is None else self.attributes.kafka_topic_names

    @kafka_topic_names.setter
    def kafka_topic_names(self, kafka_topic_names: Optional[set[str]]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.kafka_topic_names = kafka_topic_names

    @property
    def kafka_topic_qualified_names(self) -> Optional[set[str]]:
        return (
            None
            if self.attributes is None
            else self.attributes.kafka_topic_qualified_names
        )

    @kafka_topic_qualified_names.setter
    def kafka_topic_qualified_names(
        self, kafka_topic_qualified_names: Optional[set[str]]
    ):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.kafka_topic_qualified_names = kafka_topic_qualified_names

    @property
    def kafka_topics(self) -> Optional[list[KafkaTopic]]:
        return None if self.attributes is None else self.attributes.kafka_topics

    @kafka_topics.setter
    def kafka_topics(self, kafka_topics: Optional[list[KafkaTopic]]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.kafka_topics = kafka_topics

    class Attributes(Kafka.Attributes):
        kafka_consumer_group_topic_consumption_properties: Optional[
            list[KafkaTopicConsumption]
        ] = Field(
            None, description="", alias="kafkaConsumerGroupTopicConsumptionProperties"
        )
        kafka_consumer_group_member_count: Optional[int] = Field(
            None, description="", alias="kafkaConsumerGroupMemberCount"
        )
        kafka_topic_names: Optional[set[str]] = Field(
            None, description="", alias="kafkaTopicNames"
        )
        kafka_topic_qualified_names: Optional[set[str]] = Field(
            None, description="", alias="kafkaTopicQualifiedNames"
        )
        kafka_topics: Optional[list[KafkaTopic]] = Field(
            None, description="", alias="kafkaTopics"
        )  # relationship

    attributes: "KafkaConsumerGroup.Attributes" = Field(
        default_factory=lambda: KafkaConsumerGroup.Attributes(),
        description="Map of attributes in the instance and their values. The specific keys of this map will vary by "
        "type, so are described in the sub-types of this schema.\n",
    )


class KafkaTopic(Kafka):
    """Description"""

    type_name: str = Field("KafkaTopic", allow_mutation=False)

    @validator("type_name")
    def validate_type_name(cls, v):
        if v != "KafkaTopic":
            raise ValueError("must be KafkaTopic")
        return v

    def __setattr__(self, name, value):
        if name in KafkaTopic._convience_properties:
            return object.__setattr__(self, name, value)
        super().__setattr__(name, value)

    _convience_properties: ClassVar[list[str]] = [
        "kafka_topic_is_internal",
        "kafka_topic_compression_type",
        "kafka_topic_replication_factor",
        "kafka_topic_segment_bytes",
        "kafka_topic_partitions_count",
        "kafka_topic_size_in_bytes",
        "kafka_topic_record_count",
        "kafka_topic_cleanup_policy",
        "kafka_consumer_groups",
    ]

    @property
    def kafka_topic_is_internal(self) -> Optional[bool]:
        return (
            None if self.attributes is None else self.attributes.kafka_topic_is_internal
        )

    @kafka_topic_is_internal.setter
    def kafka_topic_is_internal(self, kafka_topic_is_internal: Optional[bool]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.kafka_topic_is_internal = kafka_topic_is_internal

    @property
    def kafka_topic_compression_type(self) -> Optional[KafkaTopicCompressionType]:
        return (
            None
            if self.attributes is None
            else self.attributes.kafka_topic_compression_type
        )

    @kafka_topic_compression_type.setter
    def kafka_topic_compression_type(
        self, kafka_topic_compression_type: Optional[KafkaTopicCompressionType]
    ):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.kafka_topic_compression_type = kafka_topic_compression_type

    @property
    def kafka_topic_replication_factor(self) -> Optional[int]:
        return (
            None
            if self.attributes is None
            else self.attributes.kafka_topic_replication_factor
        )

    @kafka_topic_replication_factor.setter
    def kafka_topic_replication_factor(
        self, kafka_topic_replication_factor: Optional[int]
    ):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.kafka_topic_replication_factor = kafka_topic_replication_factor

    @property
    def kafka_topic_segment_bytes(self) -> Optional[int]:
        return (
            None
            if self.attributes is None
            else self.attributes.kafka_topic_segment_bytes
        )

    @kafka_topic_segment_bytes.setter
    def kafka_topic_segment_bytes(self, kafka_topic_segment_bytes: Optional[int]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.kafka_topic_segment_bytes = kafka_topic_segment_bytes

    @property
    def kafka_topic_partitions_count(self) -> Optional[int]:
        return (
            None
            if self.attributes is None
            else self.attributes.kafka_topic_partitions_count
        )

    @kafka_topic_partitions_count.setter
    def kafka_topic_partitions_count(self, kafka_topic_partitions_count: Optional[int]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.kafka_topic_partitions_count = kafka_topic_partitions_count

    @property
    def kafka_topic_size_in_bytes(self) -> Optional[int]:
        return (
            None
            if self.attributes is None
            else self.attributes.kafka_topic_size_in_bytes
        )

    @kafka_topic_size_in_bytes.setter
    def kafka_topic_size_in_bytes(self, kafka_topic_size_in_bytes: Optional[int]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.kafka_topic_size_in_bytes = kafka_topic_size_in_bytes

    @property
    def kafka_topic_record_count(self) -> Optional[int]:
        return (
            None
            if self.attributes is None
            else self.attributes.kafka_topic_record_count
        )

    @kafka_topic_record_count.setter
    def kafka_topic_record_count(self, kafka_topic_record_count: Optional[int]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.kafka_topic_record_count = kafka_topic_record_count

    @property
    def kafka_topic_cleanup_policy(self) -> Optional[PowerbiEndorsement]:
        return (
            None
            if self.attributes is None
            else self.attributes.kafka_topic_cleanup_policy
        )

    @kafka_topic_cleanup_policy.setter
    def kafka_topic_cleanup_policy(
        self, kafka_topic_cleanup_policy: Optional[PowerbiEndorsement]
    ):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.kafka_topic_cleanup_policy = kafka_topic_cleanup_policy

    @property
    def kafka_consumer_groups(self) -> Optional[list[KafkaConsumerGroup]]:
        return (
            None if self.attributes is None else self.attributes.kafka_consumer_groups
        )

    @kafka_consumer_groups.setter
    def kafka_consumer_groups(
        self, kafka_consumer_groups: Optional[list[KafkaConsumerGroup]]
    ):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.kafka_consumer_groups = kafka_consumer_groups

    class Attributes(Kafka.Attributes):
        kafka_topic_is_internal: Optional[bool] = Field(
            None, description="", alias="kafkaTopicIsInternal"
        )
        kafka_topic_compression_type: Optional[KafkaTopicCompressionType] = Field(
            None, description="", alias="kafkaTopicCompressionType"
        )
        kafka_topic_replication_factor: Optional[int] = Field(
            None, description="", alias="kafkaTopicReplicationFactor"
        )
        kafka_topic_segment_bytes: Optional[int] = Field(
            None, description="", alias="kafkaTopicSegmentBytes"
        )
        kafka_topic_partitions_count: Optional[int] = Field(
            None, description="", alias="kafkaTopicPartitionsCount"
        )
        kafka_topic_size_in_bytes: Optional[int] = Field(
            None, description="", alias="kafkaTopicSizeInBytes"
        )
        kafka_topic_record_count: Optional[int] = Field(
            None, description="", alias="kafkaTopicRecordCount"
        )
        kafka_topic_cleanup_policy: Optional[PowerbiEndorsement] = Field(
            None, description="", alias="kafkaTopicCleanupPolicy"
        )
        kafka_consumer_groups: Optional[list[KafkaConsumerGroup]] = Field(
            None, description="", alias="kafkaConsumerGroups"
        )  # relationship

    attributes: "KafkaTopic.Attributes" = Field(
        default_factory=lambda: KafkaTopic.Attributes(),
        description="Map of attributes in the instance and their values. The specific keys of this map will vary by "
        "type, so are described in the sub-types of this schema.\n",
    )


KafkaConsumerGroup.Attributes.update_forward_refs()

KafkaTopic.Attributes.update_forward_refs()
