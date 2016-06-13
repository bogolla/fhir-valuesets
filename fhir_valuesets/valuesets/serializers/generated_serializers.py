from rest_framework.serializers import ModelSerializer
from ..models import *  # noqa


class ExampleSerializer(ModelSerializer):
    class Meta:
        model = Example


class SurfaceSerializer(ModelSerializer):
    class Meta:
        model = Surface


class Loinc480020AnswerlistSerializer(ModelSerializer):
    class Meta:
        model = Loinc480020Answerlist


class Loinc480194AnswerlistSerializer(ModelSerializer):
    class Meta:
        model = Loinc480194Answerlist


class Loinc530345AnswerlistSerializer(ModelSerializer):
    class Meta:
        model = Loinc530345Answerlist


class AbstractTypesSerializer(ModelSerializer):
    class Meta:
        model = AbstractTypes


class AccountStatusSerializer(ModelSerializer):
    class Meta:
        model = AccountStatus


class ActionBehaviorTypeSerializer(ModelSerializer):
    class Meta:
        model = ActionBehaviorType


class ActionCardinalityBehaviorSerializer(ModelSerializer):
    class Meta:
        model = ActionCardinalityBehavior


class ActionGroupingBehaviorSerializer(ModelSerializer):
    class Meta:
        model = ActionGroupingBehavior


class ActionParticipantTypeSerializer(ModelSerializer):
    class Meta:
        model = ActionParticipantType


class ActionPrecheckBehaviorSerializer(ModelSerializer):
    class Meta:
        model = ActionPrecheckBehavior


class ActionRelationshipAnchorSerializer(ModelSerializer):
    class Meta:
        model = ActionRelationshipAnchor


class ActionRelationshipTypeSerializer(ModelSerializer):
    class Meta:
        model = ActionRelationshipType


class ActionRequiredBehaviorSerializer(ModelSerializer):
    class Meta:
        model = ActionRequiredBehavior


class ActionSelectionBehaviorSerializer(ModelSerializer):
    class Meta:
        model = ActionSelectionBehavior


class ActionTypeSerializer(ModelSerializer):
    class Meta:
        model = ActionType


class ActionlistSerializer(ModelSerializer):
    class Meta:
        model = Actionlist


class ActivityDefinitionCategorySerializer(ModelSerializer):
    class Meta:
        model = ActivityDefinitionCategory


class ActivityParticipantTypeSerializer(ModelSerializer):
    class Meta:
        model = ActivityParticipantType


class AdditionalmaterialsSerializer(ModelSerializer):
    class Meta:
        model = Additionalmaterials


class AddressTypeSerializer(ModelSerializer):
    class Meta:
        model = AddressType


class AddressUseSerializer(ModelSerializer):
    class Meta:
        model = AddressUse


class AdjudicationSerializer(ModelSerializer):
    class Meta:
        model = Adjudication


class AdjudicationErrorSerializer(ModelSerializer):
    class Meta:
        model = AdjudicationError


class AdjudicationReasonSerializer(ModelSerializer):
    class Meta:
        model = AdjudicationReason


class AdministrativeGenderSerializer(ModelSerializer):
    class Meta:
        model = AdministrativeGender


class EncounterAdmitSourceSerializer(ModelSerializer):
    class Meta:
        model = EncounterAdmitSource


class AllergyIntoleranceCategorySerializer(ModelSerializer):
    class Meta:
        model = AllergyIntoleranceCategory


class AllergyIntoleranceCriticalitySerializer(ModelSerializer):
    class Meta:
        model = AllergyIntoleranceCriticality


class AllergyIntoleranceStatusSerializer(ModelSerializer):
    class Meta:
        model = AllergyIntoleranceStatus


class AllergyIntoleranceTypeSerializer(ModelSerializer):
    class Meta:
        model = AllergyIntoleranceType


class AnimalBreedsSerializer(ModelSerializer):
    class Meta:
        model = AnimalBreeds


class AnimalGenderstatusSerializer(ModelSerializer):
    class Meta:
        model = AnimalGenderstatus


class AnimalSpeciesSerializer(ModelSerializer):
    class Meta:
        model = AnimalSpecies


class AppointmentstatusSerializer(ModelSerializer):
    class Meta:
        model = Appointmentstatus


class AssertDirectionCodesSerializer(ModelSerializer):
    class Meta:
        model = AssertDirectionCodes


class AssertOperatorCodesSerializer(ModelSerializer):
    class Meta:
        model = AssertOperatorCodes


class AssertResponseCodeTypesSerializer(ModelSerializer):
    class Meta:
        model = AssertResponseCodeTypes


class AuditEventActionSerializer(ModelSerializer):
    class Meta:
        model = AuditEventAction


class AuditEventOutcomeSerializer(ModelSerializer):
    class Meta:
        model = AuditEventOutcome


class AuditEventTypeSerializer(ModelSerializer):
    class Meta:
        model = AuditEventType


class BasicResourceTypeSerializer(ModelSerializer):
    class Meta:
        model = BasicResourceType


class BenefitCategorySerializer(ModelSerializer):
    class Meta:
        model = BenefitCategory


class BenefitNetworkSerializer(ModelSerializer):
    class Meta:
        model = BenefitNetwork


class BenefitSubcategorySerializer(ModelSerializer):
    class Meta:
        model = BenefitSubcategory


class BenefitTermSerializer(ModelSerializer):
    class Meta:
        model = BenefitTerm


class BenefitTypeSerializer(ModelSerializer):
    class Meta:
        model = BenefitType


class BenefitUnitSerializer(ModelSerializer):
    class Meta:
        model = BenefitUnit


class BindingStrengthSerializer(ModelSerializer):
    class Meta:
        model = BindingStrength


class BundleTypeSerializer(ModelSerializer):
    class Meta:
        model = BundleType


class CardinalityBehaviorSerializer(ModelSerializer):
    class Meta:
        model = CardinalityBehavior


class CarePlanActivityCategorySerializer(ModelSerializer):
    class Meta:
        model = CarePlanActivityCategory


class CarePlanActivityStatusSerializer(ModelSerializer):
    class Meta:
        model = CarePlanActivityStatus


class CarePlanRelationshipSerializer(ModelSerializer):
    class Meta:
        model = CarePlanRelationship


class CarePlanStatusSerializer(ModelSerializer):
    class Meta:
        model = CarePlanStatus


class CdsRuleActionTypeSerializer(ModelSerializer):
    class Meta:
        model = CdsRuleActionType


class CdsRuleParticipantSerializer(ModelSerializer):
    class Meta:
        model = CdsRuleParticipant


class CdsRuleTriggerTypeSerializer(ModelSerializer):
    class Meta:
        model = CdsRuleTriggerType


class ChoiceListOrientationSerializer(ModelSerializer):
    class Meta:
        model = ChoiceListOrientation


class ChromosomeHumanSerializer(ModelSerializer):
    class Meta:
        model = ChromosomeHuman


class ClaimExceptionSerializer(ModelSerializer):
    class Meta:
        model = ClaimException


class ClaimTypeLinkSerializer(ModelSerializer):
    class Meta:
        model = ClaimTypeLink


class ClaimTypeLink2Serializer(ModelSerializer):
    class Meta:
        model = ClaimTypeLink2


class ClaimUseLinkSerializer(ModelSerializer):
    class Meta:
        model = ClaimUseLink


class ClaimCareteamroleSerializer(ModelSerializer):
    class Meta:
        model = ClaimCareteamrole


class ClaimInformationcategorySerializer(ModelSerializer):
    class Meta:
        model = ClaimInformationcategory


class ClassificationOrContextSerializer(ModelSerializer):
    class Meta:
        model = ClassificationOrContext


class ClinicalImpressionStatusSerializer(ModelSerializer):
    class Meta:
        model = ClinicalImpressionStatus


class ContentModeSerializer(ModelSerializer):
    class Meta:
        model = ContentMode


class CommunicationRequestStatusSerializer(ModelSerializer):
    class Meta:
        model = CommunicationRequestStatus


class CommunicationStatusSerializer(ModelSerializer):
    class Meta:
        model = CommunicationStatus


class CompartmentTypeSerializer(ModelSerializer):
    class Meta:
        model = CompartmentType


class CompositionAttestationModeSerializer(ModelSerializer):
    class Meta:
        model = CompositionAttestationMode


class CompositionStatusSerializer(ModelSerializer):
    class Meta:
        model = CompositionStatus


class ConceptMapEquivalenceSerializer(ModelSerializer):
    class Meta:
        model = ConceptMapEquivalence


class ConceptPropertiesSerializer(ModelSerializer):
    class Meta:
        model = ConceptProperties


class ConceptPropertyTypeSerializer(ModelSerializer):
    class Meta:
        model = ConceptPropertyType


class ConditionCategorySerializer(ModelSerializer):
    class Meta:
        model = ConditionCategory


class ConditionClinicalSerializer(ModelSerializer):
    class Meta:
        model = ConditionClinical


class ConditionStateSerializer(ModelSerializer):
    class Meta:
        model = ConditionState


class ConditionVerStatusSerializer(ModelSerializer):
    class Meta:
        model = ConditionVerStatus


class ConditionalDeleteStatusSerializer(ModelSerializer):
    class Meta:
        model = ConditionalDeleteStatus


class ConformanceExpectationSerializer(ModelSerializer):
    class Meta:
        model = ConformanceExpectation


class ConformanceResourceStatusSerializer(ModelSerializer):
    class Meta:
        model = ConformanceResourceStatus


class ConformanceStatementKindSerializer(ModelSerializer):
    class Meta:
        model = ConformanceStatementKind


class ConsentDataMeaningSerializer(ModelSerializer):
    class Meta:
        model = ConsentDataMeaning


class ConsentExceptTypeSerializer(ModelSerializer):
    class Meta:
        model = ConsentExceptType


class ConsentStatusSerializer(ModelSerializer):
    class Meta:
        model = ConsentStatus


class ConsentActionSerializer(ModelSerializer):
    class Meta:
        model = ConsentAction


class ConsentCategorySerializer(ModelSerializer):
    class Meta:
        model = ConsentCategory


class ConstraintSeveritySerializer(ModelSerializer):
    class Meta:
        model = ConstraintSeverity


class ContactPointSystemSerializer(ModelSerializer):
    class Meta:
        model = ContactPointSystem


class ContactPointUseSerializer(ModelSerializer):
    class Meta:
        model = ContactPointUse


class ContactentityTypeSerializer(ModelSerializer):
    class Meta:
        model = ContactentityType


class ContentTypeSerializer(ModelSerializer):
    class Meta:
        model = ContentType


class ContractSubtypeSerializer(ModelSerializer):
    class Meta:
        model = ContractSubtype


class ContractTermSubtypeSerializer(ModelSerializer):
    class Meta:
        model = ContractTermSubtype


class ContractTermTypeSerializer(ModelSerializer):
    class Meta:
        model = ContractTermType


class ContractTypeSerializer(ModelSerializer):
    class Meta:
        model = ContractType


class CopyNumberEventSerializer(ModelSerializer):
    class Meta:
        model = CopyNumberEvent


class CoverageExceptionSerializer(ModelSerializer):
    class Meta:
        model = CoverageException


class DwebtypeSerializer(ModelSerializer):
    class Meta:
        model = Dwebtype


class DataAbsentReasonSerializer(ModelSerializer):
    class Meta:
        model = DataAbsentReason


class DataTypesSerializer(ModelSerializer):
    class Meta:
        model = DataTypes


class DataelementStringencySerializer(ModelSerializer):
    class Meta:
        model = DataelementStringency


class DaysOfWeekSerializer(ModelSerializer):
    class Meta:
        model = DaysOfWeek


class DetectedissueSeveritySerializer(ModelSerializer):
    class Meta:
        model = DetectedissueSeverity


class DeviceActionSerializer(ModelSerializer):
    class Meta:
        model = DeviceAction


class DeviceUseRequestPrioritySerializer(ModelSerializer):
    class Meta:
        model = DeviceUseRequestPriority


class DeviceUseRequestStatusSerializer(ModelSerializer):
    class Meta:
        model = DeviceUseRequestStatus


class DevicestatusSerializer(ModelSerializer):
    class Meta:
        model = Devicestatus


class DiagnosticOrderPrioritySerializer(ModelSerializer):
    class Meta:
        model = DiagnosticOrderPriority


class DiagnosticOrderStatusSerializer(ModelSerializer):
    class Meta:
        model = DiagnosticOrderStatus


class DiagnosticReportStatusSerializer(ModelSerializer):
    class Meta:
        model = DiagnosticReportStatus


class EncounterDietSerializer(ModelSerializer):
    class Meta:
        model = EncounterDiet


class DigitalMediaTypeSerializer(ModelSerializer):
    class Meta:
        model = DigitalMediaType


class EncounterDischargeDispositionSerializer(ModelSerializer):
    class Meta:
        model = EncounterDischargeDisposition


class DocumentModeSerializer(ModelSerializer):
    class Meta:
        model = DocumentMode


class DocumentReferenceStatusSerializer(ModelSerializer):
    class Meta:
        model = DocumentReferenceStatus


class DocumentRelationshipTypeSerializer(ModelSerializer):
    class Meta:
        model = DocumentRelationshipType


class EncounterLocationStatusSerializer(ModelSerializer):
    class Meta:
        model = EncounterLocationStatus


class EncounterPrioritySerializer(ModelSerializer):
    class Meta:
        model = EncounterPriority


class EncounterSpecialArrangementsSerializer(ModelSerializer):
    class Meta:
        model = EncounterSpecialArrangements


class EncounterStateSerializer(ModelSerializer):
    class Meta:
        model = EncounterState


class EncounterTypeSerializer(ModelSerializer):
    class Meta:
        model = EncounterType


class EndpointStatusSerializer(ModelSerializer):
    class Meta:
        model = EndpointStatus


class EntformulaAdditiveSerializer(ModelSerializer):
    class Meta:
        model = EntformulaAdditive


class EpisodeOfCareStatusSerializer(ModelSerializer):
    class Meta:
        model = EpisodeOfCareStatus


class ServiceUsclsSerializer(ModelSerializer):
    class Meta:
        model = ServiceUscls


class FmItemtypeSerializer(ModelSerializer):
    class Meta:
        model = FmItemtype


class OccurrenceCodesSerializer(ModelSerializer):
    class Meta:
        model = OccurrenceCodes


class OccurrenceSpanCodesSerializer(ModelSerializer):
    class Meta:
        model = OccurrenceSpanCodes


class ClaimSubtypeSerializer(ModelSerializer):
    class Meta:
        model = ClaimSubtype


class ValueCodesSerializer(ModelSerializer):
    class Meta:
        model = ValueCodes


class ExDiagnosisrelatedgroupSerializer(ModelSerializer):
    class Meta:
        model = ExDiagnosisrelatedgroup


class ExDiagnosistypeSerializer(ModelSerializer):
    class Meta:
        model = ExDiagnosistype


class TeethSerializer(ModelSerializer):
    class Meta:
        model = Teeth


class ExOnsettypeSerializer(ModelSerializer):
    class Meta:
        model = ExOnsettype


class OralProsthodonticMaterialSerializer(ModelSerializer):
    class Meta:
        model = OralProsthodonticMaterial


class ExPaymenttypeSerializer(ModelSerializer):
    class Meta:
        model = ExPaymenttype


class ServicePharmacySerializer(ModelSerializer):
    class Meta:
        model = ServicePharmacy


class ExProgramCodeSerializer(ModelSerializer):
    class Meta:
        model = ExProgramCode


class ProviderQualificationSerializer(ModelSerializer):
    class Meta:
        model = ProviderQualification


class RelatedClaimRelationshipSerializer(ModelSerializer):
    class Meta:
        model = RelatedClaimRelationship


class ServiceModifiersSerializer(ModelSerializer):
    class Meta:
        model = ServiceModifiers


class ServicePlaceSerializer(ModelSerializer):
    class Meta:
        model = ServicePlace


class ServiceProductSerializer(ModelSerializer):
    class Meta:
        model = ServiceProduct


class ToothSerializer(ModelSerializer):
    class Meta:
        model = Tooth


class UdiSerializer(ModelSerializer):
    class Meta:
        model = Udi


class VisionProductSerializer(ModelSerializer):
    class Meta:
        model = VisionProduct


class ExtensionContextSerializer(ModelSerializer):
    class Meta:
        model = ExtensionContext


class FilterOperatorSerializer(ModelSerializer):
    class Meta:
        model = FilterOperator


class FlagCategorySerializer(ModelSerializer):
    class Meta:
        model = FlagCategory


class FlagPrioritySerializer(ModelSerializer):
    class Meta:
        model = FlagPriority


class FlagStatusSerializer(ModelSerializer):
    class Meta:
        model = FlagStatus


class FmConditionsSerializer(ModelSerializer):
    class Meta:
        model = FmConditions


class FormsSerializer(ModelSerializer):
    class Meta:
        model = Forms


class FundsreserveSerializer(ModelSerializer):
    class Meta:
        model = Fundsreserve


class GoalAcceptanceStatusSerializer(ModelSerializer):
    class Meta:
        model = GoalAcceptanceStatus


class GoalCategorySerializer(ModelSerializer):
    class Meta:
        model = GoalCategory


class GoalPrioritySerializer(ModelSerializer):
    class Meta:
        model = GoalPriority


class GoalRelationshipTypeSerializer(ModelSerializer):
    class Meta:
        model = GoalRelationshipType


class GoalStatusSerializer(ModelSerializer):
    class Meta:
        model = GoalStatus


class GoalStatusReasonSerializer(ModelSerializer):
    class Meta:
        model = GoalStatusReason


class GroupTypeSerializer(ModelSerializer):
    class Meta:
        model = GroupType


class GroupingBehaviorSerializer(ModelSerializer):
    class Meta:
        model = GroupingBehavior


class GuidanceResponseStatusSerializer(ModelSerializer):
    class Meta:
        model = GuidanceResponseStatus


class GuideDependencyTypeSerializer(ModelSerializer):
    class Meta:
        model = GuideDependencyType


class GuidePageKindSerializer(ModelSerializer):
    class Meta:
        model = GuidePageKind


class HistoryStatusSerializer(ModelSerializer):
    class Meta:
        model = HistoryStatus


class HttpVerbSerializer(ModelSerializer):
    class Meta:
        model = HttpVerb


class IdentifierTypeSerializer(ModelSerializer):
    class Meta:
        model = IdentifierType


class IdentifierUseSerializer(ModelSerializer):
    class Meta:
        model = IdentifierUse


class IdentityAssurancelevelSerializer(ModelSerializer):
    class Meta:
        model = IdentityAssurancelevel


class ImmunizationRecommendationDateCriterionSerializer(ModelSerializer):
    class Meta:
        model = ImmunizationRecommendationDateCriterion


class ImmunizationRecommendationStatusSerializer(ModelSerializer):
    class Meta:
        model = ImmunizationRecommendationStatus


class InterventionSerializer(ModelSerializer):
    class Meta:
        model = Intervention


class IssueSeveritySerializer(ModelSerializer):
    class Meta:
        model = IssueSeverity


class IssueTypeSerializer(ModelSerializer):
    class Meta:
        model = IssueType


class ItemTypeSerializer(ModelSerializer):
    class Meta:
        model = ItemType


class LinkTypeSerializer(ModelSerializer):
    class Meta:
        model = LinkType


class LinkageTypeSerializer(ModelSerializer):
    class Meta:
        model = LinkageType


class ListEmptyReasonSerializer(ModelSerializer):
    class Meta:
        model = ListEmptyReason


class ListExampleCodesSerializer(ModelSerializer):
    class Meta:
        model = ListExampleCodes


class ListModeSerializer(ModelSerializer):
    class Meta:
        model = ListMode


class ListOrderSerializer(ModelSerializer):
    class Meta:
        model = ListOrder


class ListStatusSerializer(ModelSerializer):
    class Meta:
        model = ListStatus


class LocationModeSerializer(ModelSerializer):
    class Meta:
        model = LocationMode


class LocationPhysicalTypeSerializer(ModelSerializer):
    class Meta:
        model = LocationPhysicalType


class LocationStatusSerializer(ModelSerializer):
    class Meta:
        model = LocationStatus


class MapContextTypeSerializer(ModelSerializer):
    class Meta:
        model = MapContextType


class MapInputModeSerializer(ModelSerializer):
    class Meta:
        model = MapInputMode


class MapListModeSerializer(ModelSerializer):
    class Meta:
        model = MapListMode


class MapModelModeSerializer(ModelSerializer):
    class Meta:
        model = MapModelMode


class MapTransformSerializer(ModelSerializer):
    class Meta:
        model = MapTransform


class MaritalStatusSerializer(ModelSerializer):
    class Meta:
        model = MaritalStatus


class MatchGradeSerializer(ModelSerializer):
    class Meta:
        model = MatchGrade


class MeasureDataUsageSerializer(ModelSerializer):
    class Meta:
        model = MeasureDataUsage


class MeasurePopulationSerializer(ModelSerializer):
    class Meta:
        model = MeasurePopulation


class MeasureReportStatusSerializer(ModelSerializer):
    class Meta:
        model = MeasureReportStatus


class MeasureReportTypeSerializer(ModelSerializer):
    class Meta:
        model = MeasureReportType


class MeasureScoringSerializer(ModelSerializer):
    class Meta:
        model = MeasureScoring


class MeasureTypeSerializer(ModelSerializer):
    class Meta:
        model = MeasureType


class MeasurementPrincipleSerializer(ModelSerializer):
    class Meta:
        model = MeasurementPrinciple


class DigitalMediaSubtypeSerializer(ModelSerializer):
    class Meta:
        model = DigitalMediaSubtype


class MedicationAdminStatusSerializer(ModelSerializer):
    class Meta:
        model = MedicationAdminStatus


class MedicationDispenseStatusSerializer(ModelSerializer):
    class Meta:
        model = MedicationDispenseStatus


class MedicationOrderStatusSerializer(ModelSerializer):
    class Meta:
        model = MedicationOrderStatus


class MedicationStatementStatusSerializer(ModelSerializer):
    class Meta:
        model = MedicationStatementStatus


class MessageConformanceEventModeSerializer(ModelSerializer):
    class Meta:
        model = MessageConformanceEventMode


class MessageEventsSerializer(ModelSerializer):
    class Meta:
        model = MessageEvents


class MessageReasonEncounterSerializer(ModelSerializer):
    class Meta:
        model = MessageReasonEncounter


class MessageSignificanceCategorySerializer(ModelSerializer):
    class Meta:
        model = MessageSignificanceCategory


class MessageTransportSerializer(ModelSerializer):
    class Meta:
        model = MessageTransport


class MetricCalibrationStateSerializer(ModelSerializer):
    class Meta:
        model = MetricCalibrationState


class MetricCalibrationTypeSerializer(ModelSerializer):
    class Meta:
        model = MetricCalibrationType


class MetricCategorySerializer(ModelSerializer):
    class Meta:
        model = MetricCategory


class MetricColorSerializer(ModelSerializer):
    class Meta:
        model = MetricColor


class MetricOperationalStatusSerializer(ModelSerializer):
    class Meta:
        model = MetricOperationalStatus


class MissingToothReasonSerializer(ModelSerializer):
    class Meta:
        model = MissingToothReason


class ClaimModifiersSerializer(ModelSerializer):
    class Meta:
        model = ClaimModifiers


class ModuleMetadataContributorSerializer(ModelSerializer):
    class Meta:
        model = ModuleMetadataContributor


class ModuleMetadataFocusTypeSerializer(ModelSerializer):
    class Meta:
        model = ModuleMetadataFocusType


class ModuleMetadataResourceTypeSerializer(ModelSerializer):
    class Meta:
        model = ModuleMetadataResourceType


class ModuleMetadataStatusSerializer(ModelSerializer):
    class Meta:
        model = ModuleMetadataStatus


class ModuleMetadataTypeSerializer(ModelSerializer):
    class Meta:
        model = ModuleMetadataType


class NameUseSerializer(ModelSerializer):
    class Meta:
        model = NameUse


class NamingsystemIdentifierTypeSerializer(ModelSerializer):
    class Meta:
        model = NamingsystemIdentifierType


class NamingsystemTypeSerializer(ModelSerializer):
    class Meta:
        model = NamingsystemType


class NarrativeStatusSerializer(ModelSerializer):
    class Meta:
        model = NarrativeStatus


class NetworkTypeSerializer(ModelSerializer):
    class Meta:
        model = NetworkType


class NoteTypeSerializer(ModelSerializer):
    class Meta:
        model = NoteType


class NutritionOrderStatusSerializer(ModelSerializer):
    class Meta:
        model = NutritionOrderStatus


class ObjectLifecycleSerializer(ModelSerializer):
    class Meta:
        model = ObjectLifecycle


class ObjectRoleSerializer(ModelSerializer):
    class Meta:
        model = ObjectRole


class ObjectTypeSerializer(ModelSerializer):
    class Meta:
        model = ObjectType


class ObservationCategorySerializer(ModelSerializer):
    class Meta:
        model = ObservationCategory


class ObservationParamcodeSerializer(ModelSerializer):
    class Meta:
        model = ObservationParamcode


class ObservationRelationshiptypesSerializer(ModelSerializer):
    class Meta:
        model = ObservationRelationshiptypes


class ObservationStatusSerializer(ModelSerializer):
    class Meta:
        model = ObservationStatus


class OperationKindSerializer(ModelSerializer):
    class Meta:
        model = OperationKind


class OperationOutcomeSerializer(ModelSerializer):
    class Meta:
        model = OperationOutcome


class OperationParameterUseSerializer(ModelSerializer):
    class Meta:
        model = OperationParameterUse


class OrderSetItemTypeSerializer(ModelSerializer):
    class Meta:
        model = OrderSetItemType


class OrderSetParticipantSerializer(ModelSerializer):
    class Meta:
        model = OrderSetParticipant


class OrderStatusSerializer(ModelSerializer):
    class Meta:
        model = OrderStatus


class OrganizationTypeSerializer(ModelSerializer):
    class Meta:
        model = OrganizationType


class EncounterParticipantTypeSerializer(ModelSerializer):
    class Meta:
        model = EncounterParticipantType


class ParticipantrequiredSerializer(ModelSerializer):
    class Meta:
        model = Participantrequired


class ParticipationstatusSerializer(ModelSerializer):
    class Meta:
        model = Participationstatus


class PatientContactRelationshipSerializer(ModelSerializer):
    class Meta:
        model = PatientContactRelationship


class PatientMpiMatchSerializer(ModelSerializer):
    class Meta:
        model = PatientMpiMatch


class PayeetypeSerializer(ModelSerializer):
    class Meta:
        model = Payeetype


class PaymentAdjustmentReasonSerializer(ModelSerializer):
    class Meta:
        model = PaymentAdjustmentReason


class PaymentTypeSerializer(ModelSerializer):
    class Meta:
        model = PaymentType


class PaymentStatusSerializer(ModelSerializer):
    class Meta:
        model = PaymentStatus


class PlanactionBehaviorTypeSerializer(ModelSerializer):
    class Meta:
        model = PlanactionBehaviorType


class PlanactionRelationshipAnchorSerializer(ModelSerializer):
    class Meta:
        model = PlanactionRelationshipAnchor


class PlanactionRelationshipTypeSerializer(ModelSerializer):
    class Meta:
        model = PlanactionRelationshipType


class PlanactionTypeSerializer(ModelSerializer):
    class Meta:
        model = PlanactionType


class PractitionerRoleSerializer(ModelSerializer):
    class Meta:
        model = PractitionerRole


class PractitionerSpecialtySerializer(ModelSerializer):
    class Meta:
        model = PractitionerSpecialty


class PrecheckBehaviorSerializer(ModelSerializer):
    class Meta:
        model = PrecheckBehavior


class ProcedureProgressStatusCodesSerializer(ModelSerializer):
    class Meta:
        model = ProcedureProgressStatusCodes


class ProcedureRelationshipTypeSerializer(ModelSerializer):
    class Meta:
        model = ProcedureRelationshipType


class ProcedureRequestPrioritySerializer(ModelSerializer):
    class Meta:
        model = ProcedureRequestPriority


class ProcedureRequestStatusSerializer(ModelSerializer):
    class Meta:
        model = ProcedureRequestStatus


class ProcedureStatusSerializer(ModelSerializer):
    class Meta:
        model = ProcedureStatus


class ProcessOutcomeSerializer(ModelSerializer):
    class Meta:
        model = ProcessOutcome


class ProcessPrioritySerializer(ModelSerializer):
    class Meta:
        model = ProcessPriority


class PropertyRepresentationSerializer(ModelSerializer):
    class Meta:
        model = PropertyRepresentation


class ProtocolActivityCategorySerializer(ModelSerializer):
    class Meta:
        model = ProtocolActivityCategory


class ProtocolStatusSerializer(ModelSerializer):
    class Meta:
        model = ProtocolStatus


class ProtocolTypeSerializer(ModelSerializer):
    class Meta:
        model = ProtocolType


class ProvenanceEntityRoleSerializer(ModelSerializer):
    class Meta:
        model = ProvenanceEntityRole


class ProvenanceAgentRoleSerializer(ModelSerializer):
    class Meta:
        model = ProvenanceAgentRole


class ProvenanceAgentTypeSerializer(ModelSerializer):
    class Meta:
        model = ProvenanceAgentType


class QuantityComparatorSerializer(ModelSerializer):
    class Meta:
        model = QuantityComparator


class QuestionMaxOccursSerializer(ModelSerializer):
    class Meta:
        model = QuestionMaxOccurs


class QuestionnaireAnswersStatusSerializer(ModelSerializer):
    class Meta:
        model = QuestionnaireAnswersStatus


class QuestionnaireDisplayCategorySerializer(ModelSerializer):
    class Meta:
        model = QuestionnaireDisplayCategory


class QuestionnaireItemControlSerializer(ModelSerializer):
    class Meta:
        model = QuestionnaireItemControl


class QuestionnaireStatusSerializer(ModelSerializer):
    class Meta:
        model = QuestionnaireStatus


class ReactionEventCertaintySerializer(ModelSerializer):
    class Meta:
        model = ReactionEventCertainty


class ReactionEventSeveritySerializer(ModelSerializer):
    class Meta:
        model = ReactionEventSeverity


class ReasonMedicationGivenCodesSerializer(ModelSerializer):
    class Meta:
        model = ReasonMedicationGivenCodes


class ReasonMedicationNotGivenCodesSerializer(ModelSerializer):
    class Meta:
        model = ReasonMedicationNotGivenCodes


class ReferenceVersionRulesSerializer(ModelSerializer):
    class Meta:
        model = ReferenceVersionRules


class ReferencerangeMeaningSerializer(ModelSerializer):
    class Meta:
        model = ReferencerangeMeaning


class ReferralcategorySerializer(ModelSerializer):
    class Meta:
        model = Referralcategory


class ReferralstatusSerializer(ModelSerializer):
    class Meta:
        model = Referralstatus


class RelationshipSerializer(ModelSerializer):
    class Meta:
        model = Relationship


class RemittanceOutcomeSerializer(ModelSerializer):
    class Meta:
        model = RemittanceOutcome


class RequiredBehaviorSerializer(ModelSerializer):
    class Meta:
        model = RequiredBehavior


class ResourceAggregationModeSerializer(ModelSerializer):
    class Meta:
        model = ResourceAggregationMode


class ResourceSlicingRulesSerializer(ModelSerializer):
    class Meta:
        model = ResourceSlicingRules


class ResourceTypeLinkSerializer(ModelSerializer):
    class Meta:
        model = ResourceTypeLink


class ResourceTypesSerializer(ModelSerializer):
    class Meta:
        model = ResourceTypes


class ResourceValidationModeSerializer(ModelSerializer):
    class Meta:
        model = ResourceValidationMode


class ResponseCodeSerializer(ModelSerializer):
    class Meta:
        model = ResponseCode


class RestfulConformanceModeSerializer(ModelSerializer):
    class Meta:
        model = RestfulConformanceMode


class RestfulInteractionSerializer(ModelSerializer):
    class Meta:
        model = RestfulInteraction


class RestfulSecurityServiceSerializer(ModelSerializer):
    class Meta:
        model = RestfulSecurityService


class RiskProbabilitySerializer(ModelSerializer):
    class Meta:
        model = RiskProbability


class RulesetSerializer(ModelSerializer):
    class Meta:
        model = Ruleset


class SearchEntryModeSerializer(ModelSerializer):
    class Meta:
        model = SearchEntryMode


class SearchModifierCodeSerializer(ModelSerializer):
    class Meta:
        model = SearchModifierCode


class SearchParamTypeSerializer(ModelSerializer):
    class Meta:
        model = SearchParamType


class SearchXpathUsageSerializer(ModelSerializer):
    class Meta:
        model = SearchXpathUsage


class AuditSourceTypeSerializer(ModelSerializer):
    class Meta:
        model = AuditSourceType


class SelectionBehaviorSerializer(ModelSerializer):
    class Meta:
        model = SelectionBehavior


class SequenceTypeSerializer(ModelSerializer):
    class Meta:
        model = SequenceType


class ServiceCategorySerializer(ModelSerializer):
    class Meta:
        model = ServiceCategory


class ServiceProvisionConditionsSerializer(ModelSerializer):
    class Meta:
        model = ServiceProvisionConditions


class ServiceReferralMethodSerializer(ModelSerializer):
    class Meta:
        model = ServiceReferralMethod


class ServiceTypeSerializer(ModelSerializer):
    class Meta:
        model = ServiceType


class Icd10ProceduresSerializer(ModelSerializer):
    class Meta:
        model = Icd10Procedures


class SlotstatusSerializer(ModelSerializer):
    class Meta:
        model = Slotstatus


class SpecialValuesSerializer(ModelSerializer):
    class Meta:
        model = SpecialValues


class SpecimenStatusSerializer(ModelSerializer):
    class Meta:
        model = SpecimenStatus


class StructureDefinitionKindSerializer(ModelSerializer):
    class Meta:
        model = StructureDefinitionKind


class SubscriptionChannelTypeSerializer(ModelSerializer):
    class Meta:
        model = SubscriptionChannelType


class SubscriptionStatusSerializer(ModelSerializer):
    class Meta:
        model = SubscriptionStatus


class SubscriptionTagSerializer(ModelSerializer):
    class Meta:
        model = SubscriptionTag


class SubstanceCategorySerializer(ModelSerializer):
    class Meta:
        model = SubstanceCategory


class SupplydeliveryTypeSerializer(ModelSerializer):
    class Meta:
        model = SupplydeliveryType


class SupplyrequestKindSerializer(ModelSerializer):
    class Meta:
        model = SupplyrequestKind


class SupplydeliveryStatusSerializer(ModelSerializer):
    class Meta:
        model = SupplydeliveryStatus


class SupplyrequestReasonSerializer(ModelSerializer):
    class Meta:
        model = SupplyrequestReason


class SupplyrequestStatusSerializer(ModelSerializer):
    class Meta:
        model = SupplyrequestStatus


class TaskPerformerTypeSerializer(ModelSerializer):
    class Meta:
        model = TaskPerformerType


class TaskPrioritySerializer(ModelSerializer):
    class Meta:
        model = TaskPriority


class TaskStageSerializer(ModelSerializer):
    class Meta:
        model = TaskStage


class TaskStatusSerializer(ModelSerializer):
    class Meta:
        model = TaskStatus


class TestscriptOperationCodesSerializer(ModelSerializer):
    class Meta:
        model = TestscriptOperationCodes


class TestscriptProfileDestinationTypesSerializer(ModelSerializer):
    class Meta:
        model = TestscriptProfileDestinationTypes


class TestscriptProfileOriginTypesSerializer(ModelSerializer):
    class Meta:
        model = TestscriptProfileOriginTypes


class TransactionModeSerializer(ModelSerializer):
    class Meta:
        model = TransactionMode


class TriggerTypeSerializer(ModelSerializer):
    class Meta:
        model = TriggerType


class TypeDerivationRuleSerializer(ModelSerializer):
    class Meta:
        model = TypeDerivationRule


class UnknownContentCodeSerializer(ModelSerializer):
    class Meta:
        model = UnknownContentCode


class VaccinationProtocolDoseStatusSerializer(ModelSerializer):
    class Meta:
        model = VaccinationProtocolDoseStatus


class VaccinationProtocolDoseStatusReasonSerializer(ModelSerializer):
    class Meta:
        model = VaccinationProtocolDoseStatusReason


class VariantStateSerializer(ModelSerializer):
    class Meta:
        model = VariantState


class VersioningPolicySerializer(ModelSerializer):
    class Meta:
        model = VersioningPolicy


class VisionBaseCodesSerializer(ModelSerializer):
    class Meta:
        model = VisionBaseCodes


class VisionEyeCodesSerializer(ModelSerializer):
    class Meta:
        model = VisionEyeCodes


class XdsRelationshipTypeSerializer(ModelSerializer):
    class Meta:
        model = XdsRelationshipType


class AcknowledgementconditionSerializer(ModelSerializer):
    class Meta:
        model = Acknowledgementcondition


class AcknowledgementdetailcodeSerializer(ModelSerializer):
    class Meta:
        model = Acknowledgementdetailcode


class AcknowledgementdetailtypeSerializer(ModelSerializer):
    class Meta:
        model = Acknowledgementdetailtype


class AcknowledgementtypeSerializer(ModelSerializer):
    class Meta:
        model = Acknowledgementtype


class ActclassSerializer(ModelSerializer):
    class Meta:
        model = Actclass


class ActcodeSerializer(ModelSerializer):
    class Meta:
        model = Actcode


class ActexposurelevelcodeSerializer(ModelSerializer):
    class Meta:
        model = Actexposurelevelcode


class ActinvoiceelementmodifierSerializer(ModelSerializer):
    class Meta:
        model = Actinvoiceelementmodifier


class ActmoodSerializer(ModelSerializer):
    class Meta:
        model = Actmood


class ActprioritySerializer(ModelSerializer):
    class Meta:
        model = Actpriority


class ActreasonSerializer(ModelSerializer):
    class Meta:
        model = Actreason


class ActrelationshipcheckpointSerializer(ModelSerializer):
    class Meta:
        model = Actrelationshipcheckpoint


class ActrelationshipjoinSerializer(ModelSerializer):
    class Meta:
        model = Actrelationshipjoin


class ActrelationshipsplitSerializer(ModelSerializer):
    class Meta:
        model = Actrelationshipsplit


class ActrelationshipsubsetSerializer(ModelSerializer):
    class Meta:
        model = Actrelationshipsubset


class ActrelationshiptypeSerializer(ModelSerializer):
    class Meta:
        model = Actrelationshiptype


class ActsiteSerializer(ModelSerializer):
    class Meta:
        model = Actsite


class ActstatusSerializer(ModelSerializer):
    class Meta:
        model = Actstatus


class ActusprivacylawSerializer(ModelSerializer):
    class Meta:
        model = Actusprivacylaw


class ActuncertaintySerializer(ModelSerializer):
    class Meta:
        model = Actuncertainty


class AddressparttypeSerializer(ModelSerializer):
    class Meta:
        model = Addressparttype


class AmericanindianalaskanativelanguagesSerializer(ModelSerializer):
    class Meta:
        model = Americanindianalaskanativelanguages


class CalendarSerializer(ModelSerializer):
    class Meta:
        model = Calendar


class CalendarcycleSerializer(ModelSerializer):
    class Meta:
        model = Calendarcycle


class CalendartypeSerializer(ModelSerializer):
    class Meta:
        model = Calendartype


class CharsetSerializer(ModelSerializer):
    class Meta:
        model = Charset


class CodingrationaleSerializer(ModelSerializer):
    class Meta:
        model = Codingrationale


class CommunicationfunctiontypeSerializer(ModelSerializer):
    class Meta:
        model = Communicationfunctiontype


class CompressionalgorithmSerializer(ModelSerializer):
    class Meta:
        model = Compressionalgorithm


class ConfidentialitySerializer(ModelSerializer):
    class Meta:
        model = Confidentiality


class ContainercapSerializer(ModelSerializer):
    class Meta:
        model = Containercap


class ContainerseparatorSerializer(ModelSerializer):
    class Meta:
        model = Containerseparator


class ContentprocessingmodeSerializer(ModelSerializer):
    class Meta:
        model = Contentprocessingmode


class ContextcontrolSerializer(ModelSerializer):
    class Meta:
        model = Contextcontrol


class DataoperationSerializer(ModelSerializer):
    class Meta:
        model = Dataoperation


class DevicealertlevelSerializer(ModelSerializer):
    class Meta:
        model = Devicealertlevel


class DocumentcompletionSerializer(ModelSerializer):
    class Meta:
        model = Documentcompletion


class DocumentstorageSerializer(ModelSerializer):
    class Meta:
        model = Documentstorage


class EducationlevelSerializer(ModelSerializer):
    class Meta:
        model = Educationlevel


class EmployeejobclassSerializer(ModelSerializer):
    class Meta:
        model = Employeejobclass


class EncounteradmissionsourceSerializer(ModelSerializer):
    class Meta:
        model = Encounteradmissionsource


class EncounterspecialcourtesySerializer(ModelSerializer):
    class Meta:
        model = Encounterspecialcourtesy


class EntityclassSerializer(ModelSerializer):
    class Meta:
        model = Entityclass


class EntitycodeSerializer(ModelSerializer):
    class Meta:
        model = Entitycode


class EntitydeterminerSerializer(ModelSerializer):
    class Meta:
        model = Entitydeterminer


class EntityhandlingSerializer(ModelSerializer):
    class Meta:
        model = Entityhandling


class EntitynamepartqualifierSerializer(ModelSerializer):
    class Meta:
        model = Entitynamepartqualifier


class Entitynamepartqualifierr2Serializer(ModelSerializer):
    class Meta:
        model = Entitynamepartqualifierr2


class EntitynameparttypeSerializer(ModelSerializer):
    class Meta:
        model = Entitynameparttype


class Entitynameparttyper2Serializer(ModelSerializer):
    class Meta:
        model = Entitynameparttyper2


class EntitynameuseSerializer(ModelSerializer):
    class Meta:
        model = Entitynameuse


class Entitynameuser2Serializer(ModelSerializer):
    class Meta:
        model = Entitynameuser2


class EntityriskSerializer(ModelSerializer):
    class Meta:
        model = Entityrisk


class EntitystatusSerializer(ModelSerializer):
    class Meta:
        model = Entitystatus


class EquipmentalertlevelSerializer(ModelSerializer):
    class Meta:
        model = Equipmentalertlevel


class EthnicitySerializer(ModelSerializer):
    class Meta:
        model = Ethnicity


class ExposuremodeSerializer(ModelSerializer):
    class Meta:
        model = Exposuremode


class GtsabbreviationSerializer(ModelSerializer):
    class Meta:
        model = Gtsabbreviation


class GenderstatusSerializer(ModelSerializer):
    class Meta:
        model = Genderstatus


class Hl7updatemodeSerializer(ModelSerializer):
    class Meta:
        model = Hl7updatemode


class HtmllinktypeSerializer(ModelSerializer):
    class Meta:
        model = Htmllinktype


class IdentifierreliabilitySerializer(ModelSerializer):
    class Meta:
        model = Identifierreliability


class IdentifierscopeSerializer(ModelSerializer):
    class Meta:
        model = Identifierscope


class IntegritycheckalgorithmSerializer(ModelSerializer):
    class Meta:
        model = Integritycheckalgorithm


class LanguageabilitymodeSerializer(ModelSerializer):
    class Meta:
        model = Languageabilitymode


class LanguageabilityproficiencySerializer(ModelSerializer):
    class Meta:
        model = Languageabilityproficiency


class LivingarrangementSerializer(ModelSerializer):
    class Meta:
        model = Livingarrangement


class LocalmarkupignoreSerializer(ModelSerializer):
    class Meta:
        model = Localmarkupignore


class LocalremotecontrolstateSerializer(ModelSerializer):
    class Meta:
        model = Localremotecontrolstate


class ManagedparticipationstatusSerializer(ModelSerializer):
    class Meta:
        model = Managedparticipationstatus


class MaprelationshipSerializer(ModelSerializer):
    class Meta:
        model = Maprelationship


class MessagewaitingprioritySerializer(ModelSerializer):
    class Meta:
        model = Messagewaitingpriority


class ModifyindicatorSerializer(ModelSerializer):
    class Meta:
        model = Modifyindicator


class NullflavorSerializer(ModelSerializer):
    class Meta:
        model = Nullflavor


class ObservationinterpretationSerializer(ModelSerializer):
    class Meta:
        model = Observationinterpretation


class ObservationmethodSerializer(ModelSerializer):
    class Meta:
        model = Observationmethod


class ObservationvalueSerializer(ModelSerializer):
    class Meta:
        model = Observationvalue


class ParticipationfunctionSerializer(ModelSerializer):
    class Meta:
        model = Participationfunction


class ParticipationmodeSerializer(ModelSerializer):
    class Meta:
        model = Participationmode


class ParticipationsignatureSerializer(ModelSerializer):
    class Meta:
        model = Participationsignature


class ParticipationtypeSerializer(ModelSerializer):
    class Meta:
        model = Participationtype


class PatientimportanceSerializer(ModelSerializer):
    class Meta:
        model = Patientimportance


class PaymenttermsSerializer(ModelSerializer):
    class Meta:
        model = Paymentterms


class PersondisabilitytypeSerializer(ModelSerializer):
    class Meta:
        model = Persondisabilitytype


class ProbabilitydistributiontypeSerializer(ModelSerializer):
    class Meta:
        model = Probabilitydistributiontype


class ProcessingidSerializer(ModelSerializer):
    class Meta:
        model = Processingid


class ProcessingmodeSerializer(ModelSerializer):
    class Meta:
        model = Processingmode


class QueryparametervalueSerializer(ModelSerializer):
    class Meta:
        model = Queryparametervalue


class QueryprioritySerializer(ModelSerializer):
    class Meta:
        model = Querypriority


class QueryrequestlimitSerializer(ModelSerializer):
    class Meta:
        model = Queryrequestlimit


class QueryresponseSerializer(ModelSerializer):
    class Meta:
        model = Queryresponse


class QuerystatuscodeSerializer(ModelSerializer):
    class Meta:
        model = Querystatuscode


class RaceSerializer(ModelSerializer):
    class Meta:
        model = Race


class RelationaloperatorSerializer(ModelSerializer):
    class Meta:
        model = Relationaloperator


class RelationshipconjunctionSerializer(ModelSerializer):
    class Meta:
        model = Relationshipconjunction


class ReligiousaffiliationSerializer(ModelSerializer):
    class Meta:
        model = Religiousaffiliation


class ResponselevelSerializer(ModelSerializer):
    class Meta:
        model = Responselevel


class ResponsemodalitySerializer(ModelSerializer):
    class Meta:
        model = Responsemodality


class ResponsemodeSerializer(ModelSerializer):
    class Meta:
        model = Responsemode


class RoleclassSerializer(ModelSerializer):
    class Meta:
        model = Roleclass


class RolecodeSerializer(ModelSerializer):
    class Meta:
        model = Rolecode


class RolelinkstatusSerializer(ModelSerializer):
    class Meta:
        model = Rolelinkstatus


class RolelinktypeSerializer(ModelSerializer):
    class Meta:
        model = Rolelinktype


class RolestatusSerializer(ModelSerializer):
    class Meta:
        model = Rolestatus


class RouteofadministrationSerializer(ModelSerializer):
    class Meta:
        model = Routeofadministration


class SequencingSerializer(ModelSerializer):
    class Meta:
        model = Sequencing


class SetoperatorSerializer(ModelSerializer):
    class Meta:
        model = Setoperator


class SpecimentypeSerializer(ModelSerializer):
    class Meta:
        model = Specimentype


class SubstitutionconditionSerializer(ModelSerializer):
    class Meta:
        model = Substitutioncondition


class TablecellhorizontalalignSerializer(ModelSerializer):
    class Meta:
        model = Tablecellhorizontalalign


class TablecellscopeSerializer(ModelSerializer):
    class Meta:
        model = Tablecellscope


class TablecellverticalalignSerializer(ModelSerializer):
    class Meta:
        model = Tablecellverticalalign


class TableframeSerializer(ModelSerializer):
    class Meta:
        model = Tableframe


class TablerulesSerializer(ModelSerializer):
    class Meta:
        model = Tablerules


class TargetawarenessSerializer(ModelSerializer):
    class Meta:
        model = Targetawareness


class TelecommunicationcapabilitiesSerializer(ModelSerializer):
    class Meta:
        model = Telecommunicationcapabilities


class TimingeventSerializer(ModelSerializer):
    class Meta:
        model = Timingevent


class TransmissionrelationshiptypecodeSerializer(ModelSerializer):
    class Meta:
        model = Transmissionrelationshiptypecode


class TribalentityusSerializer(ModelSerializer):
    class Meta:
        model = Tribalentityus


class VaccinemanufacturerSerializer(ModelSerializer):
    class Meta:
        model = Vaccinemanufacturer


class Hl7realmSerializer(ModelSerializer):
    class Meta:
        model = Hl7realm


class Hl7v3conformanceSerializer(ModelSerializer):
    class Meta:
        model = Hl7v3conformance


class OrderabledrugformSerializer(ModelSerializer):
    class Meta:
        model = Orderabledrugform


class SubstanceadminsubstitutionSerializer(ModelSerializer):
    class Meta:
        model = Substanceadminsubstitution
