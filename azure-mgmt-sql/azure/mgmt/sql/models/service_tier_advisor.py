# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .sql_sub_resource import SqlSubResource


class ServiceTierAdvisor(SqlSubResource):
    """Represents a Service Tier Advisor.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar name: Resource name
    :vartype name: str
    :ivar id: The resource ID.
    :vartype id: str
    :ivar observation_period_start: The observation period start (ISO8601
     format).
    :vartype observation_period_start: datetime
    :ivar observation_period_end: The observation period start (ISO8601
     format).
    :vartype observation_period_end: datetime
    :ivar active_time_ratio: The activeTimeRatio for service tier advisor.
    :vartype active_time_ratio: float
    :ivar min_dtu: Gets or sets minDtu for service tier advisor.
    :vartype min_dtu: float
    :ivar avg_dtu: Gets or sets avgDtu for service tier advisor.
    :vartype avg_dtu: float
    :ivar max_dtu: Gets or sets maxDtu for service tier advisor.
    :vartype max_dtu: float
    :ivar max_size_in_gb: Gets or sets maxSizeInGB for service tier advisor.
    :vartype max_size_in_gb: float
    :ivar service_level_objective_usage_metrics: Gets or sets
     serviceLevelObjectiveUsageMetrics for the service tier advisor.
    :vartype service_level_objective_usage_metrics: list of
     :class:`SloUsageMetric <azure.mgmt.sql.models.SloUsageMetric>`
    :ivar current_service_level_objective: Gets or sets
     currentServiceLevelObjective for service tier advisor.
    :vartype current_service_level_objective: str
    :ivar current_service_level_objective_id: Gets or sets
     currentServiceLevelObjectiveId for service tier advisor.
    :vartype current_service_level_objective_id: str
    :ivar usage_based_recommendation_service_level_objective: Gets or sets
     usageBasedRecommendationServiceLevelObjective for service tier advisor.
    :vartype usage_based_recommendation_service_level_objective: str
    :ivar usage_based_recommendation_service_level_objective_id: Gets or sets
     usageBasedRecommendationServiceLevelObjectiveId for service tier advisor.
    :vartype usage_based_recommendation_service_level_objective_id: str
    :ivar database_size_based_recommendation_service_level_objective: Gets or
     sets databaseSizeBasedRecommendationServiceLevelObjective for service tier
     advisor.
    :vartype database_size_based_recommendation_service_level_objective: str
    :ivar database_size_based_recommendation_service_level_objective_id: Gets
     or sets databaseSizeBasedRecommendationServiceLevelObjectiveId for service
     tier advisor.
    :vartype database_size_based_recommendation_service_level_objective_id:
     str
    :ivar disaster_plan_based_recommendation_service_level_objective: Gets or
     sets disasterPlanBasedRecommendationServiceLevelObjective for service tier
     advisor.
    :vartype disaster_plan_based_recommendation_service_level_objective: str
    :ivar disaster_plan_based_recommendation_service_level_objective_id: Gets
     or sets disasterPlanBasedRecommendationServiceLevelObjectiveId for service
     tier advisor.
    :vartype disaster_plan_based_recommendation_service_level_objective_id:
     str
    :ivar overall_recommendation_service_level_objective: Gets or sets
     overallRecommendationServiceLevelObjective for service tier advisor.
    :vartype overall_recommendation_service_level_objective: str
    :ivar overall_recommendation_service_level_objective_id: Gets or sets
     overallRecommendationServiceLevelObjectiveId for service tier advisor.
    :vartype overall_recommendation_service_level_objective_id: str
    :ivar confidence: Gets or sets confidence for service tier advisor.
    :vartype confidence: float
    """

    _validation = {
        'name': {'readonly': True},
        'id': {'readonly': True},
        'observation_period_start': {'readonly': True},
        'observation_period_end': {'readonly': True},
        'active_time_ratio': {'readonly': True},
        'min_dtu': {'readonly': True},
        'avg_dtu': {'readonly': True},
        'max_dtu': {'readonly': True},
        'max_size_in_gb': {'readonly': True},
        'service_level_objective_usage_metrics': {'readonly': True},
        'current_service_level_objective': {'readonly': True},
        'current_service_level_objective_id': {'readonly': True},
        'usage_based_recommendation_service_level_objective': {'readonly': True},
        'usage_based_recommendation_service_level_objective_id': {'readonly': True},
        'database_size_based_recommendation_service_level_objective': {'readonly': True},
        'database_size_based_recommendation_service_level_objective_id': {'readonly': True},
        'disaster_plan_based_recommendation_service_level_objective': {'readonly': True},
        'disaster_plan_based_recommendation_service_level_objective_id': {'readonly': True},
        'overall_recommendation_service_level_objective': {'readonly': True},
        'overall_recommendation_service_level_objective_id': {'readonly': True},
        'confidence': {'readonly': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'observation_period_start': {'key': 'properties.observationPeriodStart', 'type': 'iso-8601'},
        'observation_period_end': {'key': 'properties.observationPeriodEnd', 'type': 'iso-8601'},
        'active_time_ratio': {'key': 'properties.activeTimeRatio', 'type': 'float'},
        'min_dtu': {'key': 'properties.minDtu', 'type': 'float'},
        'avg_dtu': {'key': 'properties.avgDtu', 'type': 'float'},
        'max_dtu': {'key': 'properties.maxDtu', 'type': 'float'},
        'max_size_in_gb': {'key': 'properties.maxSizeInGB', 'type': 'float'},
        'service_level_objective_usage_metrics': {'key': 'properties.serviceLevelObjectiveUsageMetrics', 'type': '[SloUsageMetric]'},
        'current_service_level_objective': {'key': 'properties.currentServiceLevelObjective', 'type': 'str'},
        'current_service_level_objective_id': {'key': 'properties.currentServiceLevelObjectiveId', 'type': 'str'},
        'usage_based_recommendation_service_level_objective': {'key': 'properties.usageBasedRecommendationServiceLevelObjective', 'type': 'str'},
        'usage_based_recommendation_service_level_objective_id': {'key': 'properties.usageBasedRecommendationServiceLevelObjectiveId', 'type': 'str'},
        'database_size_based_recommendation_service_level_objective': {'key': 'properties.databaseSizeBasedRecommendationServiceLevelObjective', 'type': 'str'},
        'database_size_based_recommendation_service_level_objective_id': {'key': 'properties.databaseSizeBasedRecommendationServiceLevelObjectiveId', 'type': 'str'},
        'disaster_plan_based_recommendation_service_level_objective': {'key': 'properties.disasterPlanBasedRecommendationServiceLevelObjective', 'type': 'str'},
        'disaster_plan_based_recommendation_service_level_objective_id': {'key': 'properties.disasterPlanBasedRecommendationServiceLevelObjectiveId', 'type': 'str'},
        'overall_recommendation_service_level_objective': {'key': 'properties.overallRecommendationServiceLevelObjective', 'type': 'str'},
        'overall_recommendation_service_level_objective_id': {'key': 'properties.overallRecommendationServiceLevelObjectiveId', 'type': 'str'},
        'confidence': {'key': 'properties.confidence', 'type': 'float'},
    }

    def __init__(self):
        super(ServiceTierAdvisor, self).__init__()
        self.observation_period_start = None
        self.observation_period_end = None
        self.active_time_ratio = None
        self.min_dtu = None
        self.avg_dtu = None
        self.max_dtu = None
        self.max_size_in_gb = None
        self.service_level_objective_usage_metrics = None
        self.current_service_level_objective = None
        self.current_service_level_objective_id = None
        self.usage_based_recommendation_service_level_objective = None
        self.usage_based_recommendation_service_level_objective_id = None
        self.database_size_based_recommendation_service_level_objective = None
        self.database_size_based_recommendation_service_level_objective_id = None
        self.disaster_plan_based_recommendation_service_level_objective = None
        self.disaster_plan_based_recommendation_service_level_objective_id = None
        self.overall_recommendation_service_level_objective = None
        self.overall_recommendation_service_level_objective_id = None
        self.confidence = None
