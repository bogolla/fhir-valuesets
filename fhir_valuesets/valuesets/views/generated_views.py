from .views import CommonViewSet
from ..serializers import *  # noqa


class ExampleViewSet(CommonViewSet):
    serializer_class = ExampleSerializer
    queryset = Example.objects.all()


class SurfaceViewSet(CommonViewSet):
    serializer_class = SurfaceSerializer
    queryset = Surface.objects.all()


class Loinc480020AnswerlistViewSet(CommonViewSet):
    serializer_class = Loinc480020AnswerlistSerializer
    queryset = Loinc480020Answerlist.objects.all()


class Loinc480194AnswerlistViewSet(CommonViewSet):
    serializer_class = Loinc480194AnswerlistSerializer
    queryset = Loinc480194Answerlist.objects.all()


class Loinc530345AnswerlistViewSet(CommonViewSet):
    serializer_class = Loinc530345AnswerlistSerializer
    queryset = Loinc530345Answerlist.objects.all()


class AbstractTypesViewSet(CommonViewSet):
    serializer_class = AbstractTypesSerializer
    queryset = AbstractTypes.objects.all()


class AccountStatusViewSet(CommonViewSet):
    serializer_class = AccountStatusSerializer
    queryset = AccountStatus.objects.all()


class ActionBehaviorTypeViewSet(CommonViewSet):
    serializer_class = ActionBehaviorTypeSerializer
    queryset = ActionBehaviorType.objects.all()


class ActionCardinalityBehaviorViewSet(CommonViewSet):
    serializer_class = ActionCardinalityBehaviorSerializer
    queryset = ActionCardinalityBehavior.objects.all()


class ActionGroupingBehaviorViewSet(CommonViewSet):
    serializer_class = ActionGroupingBehaviorSerializer
    queryset = ActionGroupingBehavior.objects.all()


class ActionParticipantTypeViewSet(CommonViewSet):
    serializer_class = ActionParticipantTypeSerializer
    queryset = ActionParticipantType.objects.all()


class ActionPrecheckBehaviorViewSet(CommonViewSet):
    serializer_class = ActionPrecheckBehaviorSerializer
    queryset = ActionPrecheckBehavior.objects.all()


class ActionRelationshipAnchorViewSet(CommonViewSet):
    serializer_class = ActionRelationshipAnchorSerializer
    queryset = ActionRelationshipAnchor.objects.all()


class ActionRelationshipTypeViewSet(CommonViewSet):
    serializer_class = ActionRelationshipTypeSerializer
    queryset = ActionRelationshipType.objects.all()


class ActionRequiredBehaviorViewSet(CommonViewSet):
    serializer_class = ActionRequiredBehaviorSerializer
    queryset = ActionRequiredBehavior.objects.all()


class ActionSelectionBehaviorViewSet(CommonViewSet):
    serializer_class = ActionSelectionBehaviorSerializer
    queryset = ActionSelectionBehavior.objects.all()


class ActionTypeViewSet(CommonViewSet):
    serializer_class = ActionTypeSerializer
    queryset = ActionType.objects.all()


class ActionlistViewSet(CommonViewSet):
    serializer_class = ActionlistSerializer
    queryset = Actionlist.objects.all()


class ActivityDefinitionCategoryViewSet(CommonViewSet):
    serializer_class = ActivityDefinitionCategorySerializer
    queryset = ActivityDefinitionCategory.objects.all()


class ActivityParticipantTypeViewSet(CommonViewSet):
    serializer_class = ActivityParticipantTypeSerializer
    queryset = ActivityParticipantType.objects.all()


class AdditionalmaterialsViewSet(CommonViewSet):
    serializer_class = AdditionalmaterialsSerializer
    queryset = Additionalmaterials.objects.all()


class AddressTypeViewSet(CommonViewSet):
    serializer_class = AddressTypeSerializer
    queryset = AddressType.objects.all()


class AddressUseViewSet(CommonViewSet):
    serializer_class = AddressUseSerializer
    queryset = AddressUse.objects.all()


class AdjudicationViewSet(CommonViewSet):
    serializer_class = AdjudicationSerializer
    queryset = Adjudication.objects.all()


class AdjudicationErrorViewSet(CommonViewSet):
    serializer_class = AdjudicationErrorSerializer
    queryset = AdjudicationError.objects.all()


class AdjudicationReasonViewSet(CommonViewSet):
    serializer_class = AdjudicationReasonSerializer
    queryset = AdjudicationReason.objects.all()


class AdministrativeGenderViewSet(CommonViewSet):
    serializer_class = AdministrativeGenderSerializer
    queryset = AdministrativeGender.objects.all()


class EncounterAdmitSourceViewSet(CommonViewSet):
    serializer_class = EncounterAdmitSourceSerializer
    queryset = EncounterAdmitSource.objects.all()


class AllergyIntoleranceCategoryViewSet(CommonViewSet):
    serializer_class = AllergyIntoleranceCategorySerializer
    queryset = AllergyIntoleranceCategory.objects.all()


class AllergyIntoleranceCriticalityViewSet(CommonViewSet):
    serializer_class = AllergyIntoleranceCriticalitySerializer
    queryset = AllergyIntoleranceCriticality.objects.all()


class AllergyIntoleranceStatusViewSet(CommonViewSet):
    serializer_class = AllergyIntoleranceStatusSerializer
    queryset = AllergyIntoleranceStatus.objects.all()


class AllergyIntoleranceTypeViewSet(CommonViewSet):
    serializer_class = AllergyIntoleranceTypeSerializer
    queryset = AllergyIntoleranceType.objects.all()


class AnimalBreedsViewSet(CommonViewSet):
    serializer_class = AnimalBreedsSerializer
    queryset = AnimalBreeds.objects.all()


class AnimalGenderstatusViewSet(CommonViewSet):
    serializer_class = AnimalGenderstatusSerializer
    queryset = AnimalGenderstatus.objects.all()


class AnimalSpeciesViewSet(CommonViewSet):
    serializer_class = AnimalSpeciesSerializer
    queryset = AnimalSpecies.objects.all()


class AppointmentstatusViewSet(CommonViewSet):
    serializer_class = AppointmentstatusSerializer
    queryset = Appointmentstatus.objects.all()


class AssertDirectionCodesViewSet(CommonViewSet):
    serializer_class = AssertDirectionCodesSerializer
    queryset = AssertDirectionCodes.objects.all()


class AssertOperatorCodesViewSet(CommonViewSet):
    serializer_class = AssertOperatorCodesSerializer
    queryset = AssertOperatorCodes.objects.all()


class AssertResponseCodeTypesViewSet(CommonViewSet):
    serializer_class = AssertResponseCodeTypesSerializer
    queryset = AssertResponseCodeTypes.objects.all()


class AuditEventActionViewSet(CommonViewSet):
    serializer_class = AuditEventActionSerializer
    queryset = AuditEventAction.objects.all()


class AuditEventOutcomeViewSet(CommonViewSet):
    serializer_class = AuditEventOutcomeSerializer
    queryset = AuditEventOutcome.objects.all()


class AuditEventTypeViewSet(CommonViewSet):
    serializer_class = AuditEventTypeSerializer
    queryset = AuditEventType.objects.all()


class BasicResourceTypeViewSet(CommonViewSet):
    serializer_class = BasicResourceTypeSerializer
    queryset = BasicResourceType.objects.all()


class BenefitCategoryViewSet(CommonViewSet):
    serializer_class = BenefitCategorySerializer
    queryset = BenefitCategory.objects.all()


class BenefitNetworkViewSet(CommonViewSet):
    serializer_class = BenefitNetworkSerializer
    queryset = BenefitNetwork.objects.all()


class BenefitSubcategoryViewSet(CommonViewSet):
    serializer_class = BenefitSubcategorySerializer
    queryset = BenefitSubcategory.objects.all()


class BenefitTermViewSet(CommonViewSet):
    serializer_class = BenefitTermSerializer
    queryset = BenefitTerm.objects.all()


class BenefitTypeViewSet(CommonViewSet):
    serializer_class = BenefitTypeSerializer
    queryset = BenefitType.objects.all()


class BenefitUnitViewSet(CommonViewSet):
    serializer_class = BenefitUnitSerializer
    queryset = BenefitUnit.objects.all()


class BindingStrengthViewSet(CommonViewSet):
    serializer_class = BindingStrengthSerializer
    queryset = BindingStrength.objects.all()


class BundleTypeViewSet(CommonViewSet):
    serializer_class = BundleTypeSerializer
    queryset = BundleType.objects.all()


class CardinalityBehaviorViewSet(CommonViewSet):
    serializer_class = CardinalityBehaviorSerializer
    queryset = CardinalityBehavior.objects.all()


class CarePlanActivityCategoryViewSet(CommonViewSet):
    serializer_class = CarePlanActivityCategorySerializer
    queryset = CarePlanActivityCategory.objects.all()


class CarePlanActivityStatusViewSet(CommonViewSet):
    serializer_class = CarePlanActivityStatusSerializer
    queryset = CarePlanActivityStatus.objects.all()


class CarePlanRelationshipViewSet(CommonViewSet):
    serializer_class = CarePlanRelationshipSerializer
    queryset = CarePlanRelationship.objects.all()


class CarePlanStatusViewSet(CommonViewSet):
    serializer_class = CarePlanStatusSerializer
    queryset = CarePlanStatus.objects.all()


class CdsRuleActionTypeViewSet(CommonViewSet):
    serializer_class = CdsRuleActionTypeSerializer
    queryset = CdsRuleActionType.objects.all()


class CdsRuleParticipantViewSet(CommonViewSet):
    serializer_class = CdsRuleParticipantSerializer
    queryset = CdsRuleParticipant.objects.all()


class CdsRuleTriggerTypeViewSet(CommonViewSet):
    serializer_class = CdsRuleTriggerTypeSerializer
    queryset = CdsRuleTriggerType.objects.all()


class ChoiceListOrientationViewSet(CommonViewSet):
    serializer_class = ChoiceListOrientationSerializer
    queryset = ChoiceListOrientation.objects.all()


class ChromosomeHumanViewSet(CommonViewSet):
    serializer_class = ChromosomeHumanSerializer
    queryset = ChromosomeHuman.objects.all()


class ClaimExceptionViewSet(CommonViewSet):
    serializer_class = ClaimExceptionSerializer
    queryset = ClaimException.objects.all()


class ClaimTypeLinkViewSet(CommonViewSet):
    serializer_class = ClaimTypeLinkSerializer
    queryset = ClaimTypeLink.objects.all()


class ClaimTypeLink2ViewSet(CommonViewSet):
    serializer_class = ClaimTypeLink2Serializer
    queryset = ClaimTypeLink2.objects.all()


class ClaimUseLinkViewSet(CommonViewSet):
    serializer_class = ClaimUseLinkSerializer
    queryset = ClaimUseLink.objects.all()


class ClaimCareteamroleViewSet(CommonViewSet):
    serializer_class = ClaimCareteamroleSerializer
    queryset = ClaimCareteamrole.objects.all()


class ClaimInformationcategoryViewSet(CommonViewSet):
    serializer_class = ClaimInformationcategorySerializer
    queryset = ClaimInformationcategory.objects.all()


class ClassificationOrContextViewSet(CommonViewSet):
    serializer_class = ClassificationOrContextSerializer
    queryset = ClassificationOrContext.objects.all()


class ClinicalImpressionStatusViewSet(CommonViewSet):
    serializer_class = ClinicalImpressionStatusSerializer
    queryset = ClinicalImpressionStatus.objects.all()


class ContentModeViewSet(CommonViewSet):
    serializer_class = ContentModeSerializer
    queryset = ContentMode.objects.all()


class CommunicationRequestStatusViewSet(CommonViewSet):
    serializer_class = CommunicationRequestStatusSerializer
    queryset = CommunicationRequestStatus.objects.all()


class CommunicationStatusViewSet(CommonViewSet):
    serializer_class = CommunicationStatusSerializer
    queryset = CommunicationStatus.objects.all()


class CompartmentTypeViewSet(CommonViewSet):
    serializer_class = CompartmentTypeSerializer
    queryset = CompartmentType.objects.all()


class CompositionAttestationModeViewSet(CommonViewSet):
    serializer_class = CompositionAttestationModeSerializer
    queryset = CompositionAttestationMode.objects.all()


class CompositionStatusViewSet(CommonViewSet):
    serializer_class = CompositionStatusSerializer
    queryset = CompositionStatus.objects.all()


class ConceptMapEquivalenceViewSet(CommonViewSet):
    serializer_class = ConceptMapEquivalenceSerializer
    queryset = ConceptMapEquivalence.objects.all()


class ConceptPropertiesViewSet(CommonViewSet):
    serializer_class = ConceptPropertiesSerializer
    queryset = ConceptProperties.objects.all()


class ConceptPropertyTypeViewSet(CommonViewSet):
    serializer_class = ConceptPropertyTypeSerializer
    queryset = ConceptPropertyType.objects.all()


class ConditionCategoryViewSet(CommonViewSet):
    serializer_class = ConditionCategorySerializer
    queryset = ConditionCategory.objects.all()


class ConditionClinicalViewSet(CommonViewSet):
    serializer_class = ConditionClinicalSerializer
    queryset = ConditionClinical.objects.all()


class ConditionStateViewSet(CommonViewSet):
    serializer_class = ConditionStateSerializer
    queryset = ConditionState.objects.all()


class ConditionVerStatusViewSet(CommonViewSet):
    serializer_class = ConditionVerStatusSerializer
    queryset = ConditionVerStatus.objects.all()


class ConditionalDeleteStatusViewSet(CommonViewSet):
    serializer_class = ConditionalDeleteStatusSerializer
    queryset = ConditionalDeleteStatus.objects.all()


class ConformanceExpectationViewSet(CommonViewSet):
    serializer_class = ConformanceExpectationSerializer
    queryset = ConformanceExpectation.objects.all()


class ConformanceResourceStatusViewSet(CommonViewSet):
    serializer_class = ConformanceResourceStatusSerializer
    queryset = ConformanceResourceStatus.objects.all()


class ConformanceStatementKindViewSet(CommonViewSet):
    serializer_class = ConformanceStatementKindSerializer
    queryset = ConformanceStatementKind.objects.all()


class ConsentDataMeaningViewSet(CommonViewSet):
    serializer_class = ConsentDataMeaningSerializer
    queryset = ConsentDataMeaning.objects.all()


class ConsentExceptTypeViewSet(CommonViewSet):
    serializer_class = ConsentExceptTypeSerializer
    queryset = ConsentExceptType.objects.all()


class ConsentStatusViewSet(CommonViewSet):
    serializer_class = ConsentStatusSerializer
    queryset = ConsentStatus.objects.all()


class ConsentActionViewSet(CommonViewSet):
    serializer_class = ConsentActionSerializer
    queryset = ConsentAction.objects.all()


class ConsentCategoryViewSet(CommonViewSet):
    serializer_class = ConsentCategorySerializer
    queryset = ConsentCategory.objects.all()


class ConstraintSeverityViewSet(CommonViewSet):
    serializer_class = ConstraintSeveritySerializer
    queryset = ConstraintSeverity.objects.all()


class ContactPointSystemViewSet(CommonViewSet):
    serializer_class = ContactPointSystemSerializer
    queryset = ContactPointSystem.objects.all()


class ContactPointUseViewSet(CommonViewSet):
    serializer_class = ContactPointUseSerializer
    queryset = ContactPointUse.objects.all()


class ContactentityTypeViewSet(CommonViewSet):
    serializer_class = ContactentityTypeSerializer
    queryset = ContactentityType.objects.all()


class ContentTypeViewSet(CommonViewSet):
    serializer_class = ContentTypeSerializer
    queryset = ContentType.objects.all()


class ContractSubtypeViewSet(CommonViewSet):
    serializer_class = ContractSubtypeSerializer
    queryset = ContractSubtype.objects.all()


class ContractTermSubtypeViewSet(CommonViewSet):
    serializer_class = ContractTermSubtypeSerializer
    queryset = ContractTermSubtype.objects.all()


class ContractTermTypeViewSet(CommonViewSet):
    serializer_class = ContractTermTypeSerializer
    queryset = ContractTermType.objects.all()


class ContractTypeViewSet(CommonViewSet):
    serializer_class = ContractTypeSerializer
    queryset = ContractType.objects.all()


class CopyNumberEventViewSet(CommonViewSet):
    serializer_class = CopyNumberEventSerializer
    queryset = CopyNumberEvent.objects.all()


class CoverageExceptionViewSet(CommonViewSet):
    serializer_class = CoverageExceptionSerializer
    queryset = CoverageException.objects.all()


class DwebtypeViewSet(CommonViewSet):
    serializer_class = DwebtypeSerializer
    queryset = Dwebtype.objects.all()


class DataAbsentReasonViewSet(CommonViewSet):
    serializer_class = DataAbsentReasonSerializer
    queryset = DataAbsentReason.objects.all()


class DataTypesViewSet(CommonViewSet):
    serializer_class = DataTypesSerializer
    queryset = DataTypes.objects.all()


class DataelementStringencyViewSet(CommonViewSet):
    serializer_class = DataelementStringencySerializer
    queryset = DataelementStringency.objects.all()


class DaysOfWeekViewSet(CommonViewSet):
    serializer_class = DaysOfWeekSerializer
    queryset = DaysOfWeek.objects.all()


class DetectedissueSeverityViewSet(CommonViewSet):
    serializer_class = DetectedissueSeveritySerializer
    queryset = DetectedissueSeverity.objects.all()


class DeviceActionViewSet(CommonViewSet):
    serializer_class = DeviceActionSerializer
    queryset = DeviceAction.objects.all()


class DeviceUseRequestPriorityViewSet(CommonViewSet):
    serializer_class = DeviceUseRequestPrioritySerializer
    queryset = DeviceUseRequestPriority.objects.all()


class DeviceUseRequestStatusViewSet(CommonViewSet):
    serializer_class = DeviceUseRequestStatusSerializer
    queryset = DeviceUseRequestStatus.objects.all()


class DevicestatusViewSet(CommonViewSet):
    serializer_class = DevicestatusSerializer
    queryset = Devicestatus.objects.all()


class DiagnosticOrderPriorityViewSet(CommonViewSet):
    serializer_class = DiagnosticOrderPrioritySerializer
    queryset = DiagnosticOrderPriority.objects.all()


class DiagnosticOrderStatusViewSet(CommonViewSet):
    serializer_class = DiagnosticOrderStatusSerializer
    queryset = DiagnosticOrderStatus.objects.all()


class DiagnosticReportStatusViewSet(CommonViewSet):
    serializer_class = DiagnosticReportStatusSerializer
    queryset = DiagnosticReportStatus.objects.all()


class EncounterDietViewSet(CommonViewSet):
    serializer_class = EncounterDietSerializer
    queryset = EncounterDiet.objects.all()


class DigitalMediaTypeViewSet(CommonViewSet):
    serializer_class = DigitalMediaTypeSerializer
    queryset = DigitalMediaType.objects.all()


class EncounterDischargeDispositionViewSet(CommonViewSet):
    serializer_class = EncounterDischargeDispositionSerializer
    queryset = EncounterDischargeDisposition.objects.all()


class DocumentModeViewSet(CommonViewSet):
    serializer_class = DocumentModeSerializer
    queryset = DocumentMode.objects.all()


class DocumentReferenceStatusViewSet(CommonViewSet):
    serializer_class = DocumentReferenceStatusSerializer
    queryset = DocumentReferenceStatus.objects.all()


class DocumentRelationshipTypeViewSet(CommonViewSet):
    serializer_class = DocumentRelationshipTypeSerializer
    queryset = DocumentRelationshipType.objects.all()


class EncounterLocationStatusViewSet(CommonViewSet):
    serializer_class = EncounterLocationStatusSerializer
    queryset = EncounterLocationStatus.objects.all()


class EncounterPriorityViewSet(CommonViewSet):
    serializer_class = EncounterPrioritySerializer
    queryset = EncounterPriority.objects.all()


class EncounterSpecialArrangementsViewSet(CommonViewSet):
    serializer_class = EncounterSpecialArrangementsSerializer
    queryset = EncounterSpecialArrangements.objects.all()


class EncounterStateViewSet(CommonViewSet):
    serializer_class = EncounterStateSerializer
    queryset = EncounterState.objects.all()


class EncounterTypeViewSet(CommonViewSet):
    serializer_class = EncounterTypeSerializer
    queryset = EncounterType.objects.all()


class EndpointStatusViewSet(CommonViewSet):
    serializer_class = EndpointStatusSerializer
    queryset = EndpointStatus.objects.all()


class EntformulaAdditiveViewSet(CommonViewSet):
    serializer_class = EntformulaAdditiveSerializer
    queryset = EntformulaAdditive.objects.all()


class EpisodeOfCareStatusViewSet(CommonViewSet):
    serializer_class = EpisodeOfCareStatusSerializer
    queryset = EpisodeOfCareStatus.objects.all()


class ServiceUsclsViewSet(CommonViewSet):
    serializer_class = ServiceUsclsSerializer
    queryset = ServiceUscls.objects.all()


class FmItemtypeViewSet(CommonViewSet):
    serializer_class = FmItemtypeSerializer
    queryset = FmItemtype.objects.all()


class OccurrenceCodesViewSet(CommonViewSet):
    serializer_class = OccurrenceCodesSerializer
    queryset = OccurrenceCodes.objects.all()


class OccurrenceSpanCodesViewSet(CommonViewSet):
    serializer_class = OccurrenceSpanCodesSerializer
    queryset = OccurrenceSpanCodes.objects.all()


class ClaimSubtypeViewSet(CommonViewSet):
    serializer_class = ClaimSubtypeSerializer
    queryset = ClaimSubtype.objects.all()


class ValueCodesViewSet(CommonViewSet):
    serializer_class = ValueCodesSerializer
    queryset = ValueCodes.objects.all()


class ExDiagnosisrelatedgroupViewSet(CommonViewSet):
    serializer_class = ExDiagnosisrelatedgroupSerializer
    queryset = ExDiagnosisrelatedgroup.objects.all()


class ExDiagnosistypeViewSet(CommonViewSet):
    serializer_class = ExDiagnosistypeSerializer
    queryset = ExDiagnosistype.objects.all()


class TeethViewSet(CommonViewSet):
    serializer_class = TeethSerializer
    queryset = Teeth.objects.all()


class ExOnsettypeViewSet(CommonViewSet):
    serializer_class = ExOnsettypeSerializer
    queryset = ExOnsettype.objects.all()


class OralProsthodonticMaterialViewSet(CommonViewSet):
    serializer_class = OralProsthodonticMaterialSerializer
    queryset = OralProsthodonticMaterial.objects.all()


class ExPaymenttypeViewSet(CommonViewSet):
    serializer_class = ExPaymenttypeSerializer
    queryset = ExPaymenttype.objects.all()


class ServicePharmacyViewSet(CommonViewSet):
    serializer_class = ServicePharmacySerializer
    queryset = ServicePharmacy.objects.all()


class ExProgramCodeViewSet(CommonViewSet):
    serializer_class = ExProgramCodeSerializer
    queryset = ExProgramCode.objects.all()


class ProviderQualificationViewSet(CommonViewSet):
    serializer_class = ProviderQualificationSerializer
    queryset = ProviderQualification.objects.all()


class RelatedClaimRelationshipViewSet(CommonViewSet):
    serializer_class = RelatedClaimRelationshipSerializer
    queryset = RelatedClaimRelationship.objects.all()


class ServiceModifiersViewSet(CommonViewSet):
    serializer_class = ServiceModifiersSerializer
    queryset = ServiceModifiers.objects.all()


class ServicePlaceViewSet(CommonViewSet):
    serializer_class = ServicePlaceSerializer
    queryset = ServicePlace.objects.all()


class ServiceProductViewSet(CommonViewSet):
    serializer_class = ServiceProductSerializer
    queryset = ServiceProduct.objects.all()


class ToothViewSet(CommonViewSet):
    serializer_class = ToothSerializer
    queryset = Tooth.objects.all()


class UdiViewSet(CommonViewSet):
    serializer_class = UdiSerializer
    queryset = Udi.objects.all()


class VisionProductViewSet(CommonViewSet):
    serializer_class = VisionProductSerializer
    queryset = VisionProduct.objects.all()


class ExtensionContextViewSet(CommonViewSet):
    serializer_class = ExtensionContextSerializer
    queryset = ExtensionContext.objects.all()


class FilterOperatorViewSet(CommonViewSet):
    serializer_class = FilterOperatorSerializer
    queryset = FilterOperator.objects.all()


class FlagCategoryViewSet(CommonViewSet):
    serializer_class = FlagCategorySerializer
    queryset = FlagCategory.objects.all()


class FlagPriorityViewSet(CommonViewSet):
    serializer_class = FlagPrioritySerializer
    queryset = FlagPriority.objects.all()


class FlagStatusViewSet(CommonViewSet):
    serializer_class = FlagStatusSerializer
    queryset = FlagStatus.objects.all()


class FmConditionsViewSet(CommonViewSet):
    serializer_class = FmConditionsSerializer
    queryset = FmConditions.objects.all()


class FormsViewSet(CommonViewSet):
    serializer_class = FormsSerializer
    queryset = Forms.objects.all()


class FundsreserveViewSet(CommonViewSet):
    serializer_class = FundsreserveSerializer
    queryset = Fundsreserve.objects.all()


class GoalAcceptanceStatusViewSet(CommonViewSet):
    serializer_class = GoalAcceptanceStatusSerializer
    queryset = GoalAcceptanceStatus.objects.all()


class GoalCategoryViewSet(CommonViewSet):
    serializer_class = GoalCategorySerializer
    queryset = GoalCategory.objects.all()


class GoalPriorityViewSet(CommonViewSet):
    serializer_class = GoalPrioritySerializer
    queryset = GoalPriority.objects.all()


class GoalRelationshipTypeViewSet(CommonViewSet):
    serializer_class = GoalRelationshipTypeSerializer
    queryset = GoalRelationshipType.objects.all()


class GoalStatusViewSet(CommonViewSet):
    serializer_class = GoalStatusSerializer
    queryset = GoalStatus.objects.all()


class GoalStatusReasonViewSet(CommonViewSet):
    serializer_class = GoalStatusReasonSerializer
    queryset = GoalStatusReason.objects.all()


class GroupTypeViewSet(CommonViewSet):
    serializer_class = GroupTypeSerializer
    queryset = GroupType.objects.all()


class GroupingBehaviorViewSet(CommonViewSet):
    serializer_class = GroupingBehaviorSerializer
    queryset = GroupingBehavior.objects.all()


class GuidanceResponseStatusViewSet(CommonViewSet):
    serializer_class = GuidanceResponseStatusSerializer
    queryset = GuidanceResponseStatus.objects.all()


class GuideDependencyTypeViewSet(CommonViewSet):
    serializer_class = GuideDependencyTypeSerializer
    queryset = GuideDependencyType.objects.all()


class GuidePageKindViewSet(CommonViewSet):
    serializer_class = GuidePageKindSerializer
    queryset = GuidePageKind.objects.all()


class HistoryStatusViewSet(CommonViewSet):
    serializer_class = HistoryStatusSerializer
    queryset = HistoryStatus.objects.all()


class HttpVerbViewSet(CommonViewSet):
    serializer_class = HttpVerbSerializer
    queryset = HttpVerb.objects.all()


class IdentifierTypeViewSet(CommonViewSet):
    serializer_class = IdentifierTypeSerializer
    queryset = IdentifierType.objects.all()


class IdentifierUseViewSet(CommonViewSet):
    serializer_class = IdentifierUseSerializer
    queryset = IdentifierUse.objects.all()


class IdentityAssurancelevelViewSet(CommonViewSet):
    serializer_class = IdentityAssurancelevelSerializer
    queryset = IdentityAssurancelevel.objects.all()


class ImmunizationRecommendationDateCriterionViewSet(CommonViewSet):
    serializer_class = ImmunizationRecommendationDateCriterionSerializer
    queryset = ImmunizationRecommendationDateCriterion.objects.all()


class ImmunizationRecommendationStatusViewSet(CommonViewSet):
    serializer_class = ImmunizationRecommendationStatusSerializer
    queryset = ImmunizationRecommendationStatus.objects.all()


class InterventionViewSet(CommonViewSet):
    serializer_class = InterventionSerializer
    queryset = Intervention.objects.all()


class IssueSeverityViewSet(CommonViewSet):
    serializer_class = IssueSeveritySerializer
    queryset = IssueSeverity.objects.all()


class IssueTypeViewSet(CommonViewSet):
    serializer_class = IssueTypeSerializer
    queryset = IssueType.objects.all()


class ItemTypeViewSet(CommonViewSet):
    serializer_class = ItemTypeSerializer
    queryset = ItemType.objects.all()


class LinkTypeViewSet(CommonViewSet):
    serializer_class = LinkTypeSerializer
    queryset = LinkType.objects.all()


class LinkageTypeViewSet(CommonViewSet):
    serializer_class = LinkageTypeSerializer
    queryset = LinkageType.objects.all()


class ListEmptyReasonViewSet(CommonViewSet):
    serializer_class = ListEmptyReasonSerializer
    queryset = ListEmptyReason.objects.all()


class ListExampleCodesViewSet(CommonViewSet):
    serializer_class = ListExampleCodesSerializer
    queryset = ListExampleCodes.objects.all()


class ListModeViewSet(CommonViewSet):
    serializer_class = ListModeSerializer
    queryset = ListMode.objects.all()


class ListOrderViewSet(CommonViewSet):
    serializer_class = ListOrderSerializer
    queryset = ListOrder.objects.all()


class ListStatusViewSet(CommonViewSet):
    serializer_class = ListStatusSerializer
    queryset = ListStatus.objects.all()


class LocationModeViewSet(CommonViewSet):
    serializer_class = LocationModeSerializer
    queryset = LocationMode.objects.all()


class LocationPhysicalTypeViewSet(CommonViewSet):
    serializer_class = LocationPhysicalTypeSerializer
    queryset = LocationPhysicalType.objects.all()


class LocationStatusViewSet(CommonViewSet):
    serializer_class = LocationStatusSerializer
    queryset = LocationStatus.objects.all()


class MapContextTypeViewSet(CommonViewSet):
    serializer_class = MapContextTypeSerializer
    queryset = MapContextType.objects.all()


class MapInputModeViewSet(CommonViewSet):
    serializer_class = MapInputModeSerializer
    queryset = MapInputMode.objects.all()


class MapListModeViewSet(CommonViewSet):
    serializer_class = MapListModeSerializer
    queryset = MapListMode.objects.all()


class MapModelModeViewSet(CommonViewSet):
    serializer_class = MapModelModeSerializer
    queryset = MapModelMode.objects.all()


class MapTransformViewSet(CommonViewSet):
    serializer_class = MapTransformSerializer
    queryset = MapTransform.objects.all()


class MaritalStatusViewSet(CommonViewSet):
    serializer_class = MaritalStatusSerializer
    queryset = MaritalStatus.objects.all()


class MatchGradeViewSet(CommonViewSet):
    serializer_class = MatchGradeSerializer
    queryset = MatchGrade.objects.all()


class MeasureDataUsageViewSet(CommonViewSet):
    serializer_class = MeasureDataUsageSerializer
    queryset = MeasureDataUsage.objects.all()


class MeasurePopulationViewSet(CommonViewSet):
    serializer_class = MeasurePopulationSerializer
    queryset = MeasurePopulation.objects.all()


class MeasureReportStatusViewSet(CommonViewSet):
    serializer_class = MeasureReportStatusSerializer
    queryset = MeasureReportStatus.objects.all()


class MeasureReportTypeViewSet(CommonViewSet):
    serializer_class = MeasureReportTypeSerializer
    queryset = MeasureReportType.objects.all()


class MeasureScoringViewSet(CommonViewSet):
    serializer_class = MeasureScoringSerializer
    queryset = MeasureScoring.objects.all()


class MeasureTypeViewSet(CommonViewSet):
    serializer_class = MeasureTypeSerializer
    queryset = MeasureType.objects.all()


class MeasurementPrincipleViewSet(CommonViewSet):
    serializer_class = MeasurementPrincipleSerializer
    queryset = MeasurementPrinciple.objects.all()


class DigitalMediaSubtypeViewSet(CommonViewSet):
    serializer_class = DigitalMediaSubtypeSerializer
    queryset = DigitalMediaSubtype.objects.all()


class MedicationAdminStatusViewSet(CommonViewSet):
    serializer_class = MedicationAdminStatusSerializer
    queryset = MedicationAdminStatus.objects.all()


class MedicationDispenseStatusViewSet(CommonViewSet):
    serializer_class = MedicationDispenseStatusSerializer
    queryset = MedicationDispenseStatus.objects.all()


class MedicationOrderStatusViewSet(CommonViewSet):
    serializer_class = MedicationOrderStatusSerializer
    queryset = MedicationOrderStatus.objects.all()


class MedicationStatementStatusViewSet(CommonViewSet):
    serializer_class = MedicationStatementStatusSerializer
    queryset = MedicationStatementStatus.objects.all()


class MessageConformanceEventModeViewSet(CommonViewSet):
    serializer_class = MessageConformanceEventModeSerializer
    queryset = MessageConformanceEventMode.objects.all()


class MessageEventsViewSet(CommonViewSet):
    serializer_class = MessageEventsSerializer
    queryset = MessageEvents.objects.all()


class MessageReasonEncounterViewSet(CommonViewSet):
    serializer_class = MessageReasonEncounterSerializer
    queryset = MessageReasonEncounter.objects.all()


class MessageSignificanceCategoryViewSet(CommonViewSet):
    serializer_class = MessageSignificanceCategorySerializer
    queryset = MessageSignificanceCategory.objects.all()


class MessageTransportViewSet(CommonViewSet):
    serializer_class = MessageTransportSerializer
    queryset = MessageTransport.objects.all()


class MetricCalibrationStateViewSet(CommonViewSet):
    serializer_class = MetricCalibrationStateSerializer
    queryset = MetricCalibrationState.objects.all()


class MetricCalibrationTypeViewSet(CommonViewSet):
    serializer_class = MetricCalibrationTypeSerializer
    queryset = MetricCalibrationType.objects.all()


class MetricCategoryViewSet(CommonViewSet):
    serializer_class = MetricCategorySerializer
    queryset = MetricCategory.objects.all()


class MetricColorViewSet(CommonViewSet):
    serializer_class = MetricColorSerializer
    queryset = MetricColor.objects.all()


class MetricOperationalStatusViewSet(CommonViewSet):
    serializer_class = MetricOperationalStatusSerializer
    queryset = MetricOperationalStatus.objects.all()


class MissingToothReasonViewSet(CommonViewSet):
    serializer_class = MissingToothReasonSerializer
    queryset = MissingToothReason.objects.all()


class ClaimModifiersViewSet(CommonViewSet):
    serializer_class = ClaimModifiersSerializer
    queryset = ClaimModifiers.objects.all()


class ModuleMetadataContributorViewSet(CommonViewSet):
    serializer_class = ModuleMetadataContributorSerializer
    queryset = ModuleMetadataContributor.objects.all()


class ModuleMetadataFocusTypeViewSet(CommonViewSet):
    serializer_class = ModuleMetadataFocusTypeSerializer
    queryset = ModuleMetadataFocusType.objects.all()


class ModuleMetadataResourceTypeViewSet(CommonViewSet):
    serializer_class = ModuleMetadataResourceTypeSerializer
    queryset = ModuleMetadataResourceType.objects.all()


class ModuleMetadataStatusViewSet(CommonViewSet):
    serializer_class = ModuleMetadataStatusSerializer
    queryset = ModuleMetadataStatus.objects.all()


class ModuleMetadataTypeViewSet(CommonViewSet):
    serializer_class = ModuleMetadataTypeSerializer
    queryset = ModuleMetadataType.objects.all()


class NameUseViewSet(CommonViewSet):
    serializer_class = NameUseSerializer
    queryset = NameUse.objects.all()


class NamingsystemIdentifierTypeViewSet(CommonViewSet):
    serializer_class = NamingsystemIdentifierTypeSerializer
    queryset = NamingsystemIdentifierType.objects.all()


class NamingsystemTypeViewSet(CommonViewSet):
    serializer_class = NamingsystemTypeSerializer
    queryset = NamingsystemType.objects.all()


class NarrativeStatusViewSet(CommonViewSet):
    serializer_class = NarrativeStatusSerializer
    queryset = NarrativeStatus.objects.all()


class NetworkTypeViewSet(CommonViewSet):
    serializer_class = NetworkTypeSerializer
    queryset = NetworkType.objects.all()


class NoteTypeViewSet(CommonViewSet):
    serializer_class = NoteTypeSerializer
    queryset = NoteType.objects.all()


class NutritionOrderStatusViewSet(CommonViewSet):
    serializer_class = NutritionOrderStatusSerializer
    queryset = NutritionOrderStatus.objects.all()


class ObjectLifecycleViewSet(CommonViewSet):
    serializer_class = ObjectLifecycleSerializer
    queryset = ObjectLifecycle.objects.all()


class ObjectRoleViewSet(CommonViewSet):
    serializer_class = ObjectRoleSerializer
    queryset = ObjectRole.objects.all()


class ObjectTypeViewSet(CommonViewSet):
    serializer_class = ObjectTypeSerializer
    queryset = ObjectType.objects.all()


class ObservationCategoryViewSet(CommonViewSet):
    serializer_class = ObservationCategorySerializer
    queryset = ObservationCategory.objects.all()


class ObservationParamcodeViewSet(CommonViewSet):
    serializer_class = ObservationParamcodeSerializer
    queryset = ObservationParamcode.objects.all()


class ObservationRelationshiptypesViewSet(CommonViewSet):
    serializer_class = ObservationRelationshiptypesSerializer
    queryset = ObservationRelationshiptypes.objects.all()


class ObservationStatusViewSet(CommonViewSet):
    serializer_class = ObservationStatusSerializer
    queryset = ObservationStatus.objects.all()


class OperationKindViewSet(CommonViewSet):
    serializer_class = OperationKindSerializer
    queryset = OperationKind.objects.all()


class OperationOutcomeViewSet(CommonViewSet):
    serializer_class = OperationOutcomeSerializer
    queryset = OperationOutcome.objects.all()


class OperationParameterUseViewSet(CommonViewSet):
    serializer_class = OperationParameterUseSerializer
    queryset = OperationParameterUse.objects.all()


class OrderSetItemTypeViewSet(CommonViewSet):
    serializer_class = OrderSetItemTypeSerializer
    queryset = OrderSetItemType.objects.all()


class OrderSetParticipantViewSet(CommonViewSet):
    serializer_class = OrderSetParticipantSerializer
    queryset = OrderSetParticipant.objects.all()


class OrderStatusViewSet(CommonViewSet):
    serializer_class = OrderStatusSerializer
    queryset = OrderStatus.objects.all()


class OrganizationTypeViewSet(CommonViewSet):
    serializer_class = OrganizationTypeSerializer
    queryset = OrganizationType.objects.all()


class EncounterParticipantTypeViewSet(CommonViewSet):
    serializer_class = EncounterParticipantTypeSerializer
    queryset = EncounterParticipantType.objects.all()


class ParticipantrequiredViewSet(CommonViewSet):
    serializer_class = ParticipantrequiredSerializer
    queryset = Participantrequired.objects.all()


class ParticipationstatusViewSet(CommonViewSet):
    serializer_class = ParticipationstatusSerializer
    queryset = Participationstatus.objects.all()


class PatientContactRelationshipViewSet(CommonViewSet):
    serializer_class = PatientContactRelationshipSerializer
    queryset = PatientContactRelationship.objects.all()


class PatientMpiMatchViewSet(CommonViewSet):
    serializer_class = PatientMpiMatchSerializer
    queryset = PatientMpiMatch.objects.all()


class PayeetypeViewSet(CommonViewSet):
    serializer_class = PayeetypeSerializer
    queryset = Payeetype.objects.all()


class PaymentAdjustmentReasonViewSet(CommonViewSet):
    serializer_class = PaymentAdjustmentReasonSerializer
    queryset = PaymentAdjustmentReason.objects.all()


class PaymentTypeViewSet(CommonViewSet):
    serializer_class = PaymentTypeSerializer
    queryset = PaymentType.objects.all()


class PaymentStatusViewSet(CommonViewSet):
    serializer_class = PaymentStatusSerializer
    queryset = PaymentStatus.objects.all()


class PlanactionBehaviorTypeViewSet(CommonViewSet):
    serializer_class = PlanactionBehaviorTypeSerializer
    queryset = PlanactionBehaviorType.objects.all()


class PlanactionRelationshipAnchorViewSet(CommonViewSet):
    serializer_class = PlanactionRelationshipAnchorSerializer
    queryset = PlanactionRelationshipAnchor.objects.all()


class PlanactionRelationshipTypeViewSet(CommonViewSet):
    serializer_class = PlanactionRelationshipTypeSerializer
    queryset = PlanactionRelationshipType.objects.all()


class PlanactionTypeViewSet(CommonViewSet):
    serializer_class = PlanactionTypeSerializer
    queryset = PlanactionType.objects.all()


class PractitionerRoleViewSet(CommonViewSet):
    serializer_class = PractitionerRoleSerializer
    queryset = PractitionerRole.objects.all()


class PractitionerSpecialtyViewSet(CommonViewSet):
    serializer_class = PractitionerSpecialtySerializer
    queryset = PractitionerSpecialty.objects.all()


class PrecheckBehaviorViewSet(CommonViewSet):
    serializer_class = PrecheckBehaviorSerializer
    queryset = PrecheckBehavior.objects.all()


class ProcedureProgressStatusCodesViewSet(CommonViewSet):
    serializer_class = ProcedureProgressStatusCodesSerializer
    queryset = ProcedureProgressStatusCodes.objects.all()


class ProcedureRelationshipTypeViewSet(CommonViewSet):
    serializer_class = ProcedureRelationshipTypeSerializer
    queryset = ProcedureRelationshipType.objects.all()


class ProcedureRequestPriorityViewSet(CommonViewSet):
    serializer_class = ProcedureRequestPrioritySerializer
    queryset = ProcedureRequestPriority.objects.all()


class ProcedureRequestStatusViewSet(CommonViewSet):
    serializer_class = ProcedureRequestStatusSerializer
    queryset = ProcedureRequestStatus.objects.all()


class ProcedureStatusViewSet(CommonViewSet):
    serializer_class = ProcedureStatusSerializer
    queryset = ProcedureStatus.objects.all()


class ProcessOutcomeViewSet(CommonViewSet):
    serializer_class = ProcessOutcomeSerializer
    queryset = ProcessOutcome.objects.all()


class ProcessPriorityViewSet(CommonViewSet):
    serializer_class = ProcessPrioritySerializer
    queryset = ProcessPriority.objects.all()


class PropertyRepresentationViewSet(CommonViewSet):
    serializer_class = PropertyRepresentationSerializer
    queryset = PropertyRepresentation.objects.all()


class ProtocolActivityCategoryViewSet(CommonViewSet):
    serializer_class = ProtocolActivityCategorySerializer
    queryset = ProtocolActivityCategory.objects.all()


class ProtocolStatusViewSet(CommonViewSet):
    serializer_class = ProtocolStatusSerializer
    queryset = ProtocolStatus.objects.all()


class ProtocolTypeViewSet(CommonViewSet):
    serializer_class = ProtocolTypeSerializer
    queryset = ProtocolType.objects.all()


class ProvenanceEntityRoleViewSet(CommonViewSet):
    serializer_class = ProvenanceEntityRoleSerializer
    queryset = ProvenanceEntityRole.objects.all()


class ProvenanceAgentRoleViewSet(CommonViewSet):
    serializer_class = ProvenanceAgentRoleSerializer
    queryset = ProvenanceAgentRole.objects.all()


class ProvenanceAgentTypeViewSet(CommonViewSet):
    serializer_class = ProvenanceAgentTypeSerializer
    queryset = ProvenanceAgentType.objects.all()


class QuantityComparatorViewSet(CommonViewSet):
    serializer_class = QuantityComparatorSerializer
    queryset = QuantityComparator.objects.all()


class QuestionMaxOccursViewSet(CommonViewSet):
    serializer_class = QuestionMaxOccursSerializer
    queryset = QuestionMaxOccurs.objects.all()


class QuestionnaireAnswersStatusViewSet(CommonViewSet):
    serializer_class = QuestionnaireAnswersStatusSerializer
    queryset = QuestionnaireAnswersStatus.objects.all()


class QuestionnaireDisplayCategoryViewSet(CommonViewSet):
    serializer_class = QuestionnaireDisplayCategorySerializer
    queryset = QuestionnaireDisplayCategory.objects.all()


class QuestionnaireItemControlViewSet(CommonViewSet):
    serializer_class = QuestionnaireItemControlSerializer
    queryset = QuestionnaireItemControl.objects.all()


class QuestionnaireStatusViewSet(CommonViewSet):
    serializer_class = QuestionnaireStatusSerializer
    queryset = QuestionnaireStatus.objects.all()


class ReactionEventCertaintyViewSet(CommonViewSet):
    serializer_class = ReactionEventCertaintySerializer
    queryset = ReactionEventCertainty.objects.all()


class ReactionEventSeverityViewSet(CommonViewSet):
    serializer_class = ReactionEventSeveritySerializer
    queryset = ReactionEventSeverity.objects.all()


class ReasonMedicationGivenCodesViewSet(CommonViewSet):
    serializer_class = ReasonMedicationGivenCodesSerializer
    queryset = ReasonMedicationGivenCodes.objects.all()


class ReasonMedicationNotGivenCodesViewSet(CommonViewSet):
    serializer_class = ReasonMedicationNotGivenCodesSerializer
    queryset = ReasonMedicationNotGivenCodes.objects.all()


class ReferenceVersionRulesViewSet(CommonViewSet):
    serializer_class = ReferenceVersionRulesSerializer
    queryset = ReferenceVersionRules.objects.all()


class ReferencerangeMeaningViewSet(CommonViewSet):
    serializer_class = ReferencerangeMeaningSerializer
    queryset = ReferencerangeMeaning.objects.all()


class ReferralcategoryViewSet(CommonViewSet):
    serializer_class = ReferralcategorySerializer
    queryset = Referralcategory.objects.all()


class ReferralstatusViewSet(CommonViewSet):
    serializer_class = ReferralstatusSerializer
    queryset = Referralstatus.objects.all()


class RelationshipViewSet(CommonViewSet):
    serializer_class = RelationshipSerializer
    queryset = Relationship.objects.all()


class RemittanceOutcomeViewSet(CommonViewSet):
    serializer_class = RemittanceOutcomeSerializer
    queryset = RemittanceOutcome.objects.all()


class RequiredBehaviorViewSet(CommonViewSet):
    serializer_class = RequiredBehaviorSerializer
    queryset = RequiredBehavior.objects.all()


class ResourceAggregationModeViewSet(CommonViewSet):
    serializer_class = ResourceAggregationModeSerializer
    queryset = ResourceAggregationMode.objects.all()


class ResourceSlicingRulesViewSet(CommonViewSet):
    serializer_class = ResourceSlicingRulesSerializer
    queryset = ResourceSlicingRules.objects.all()


class ResourceTypeLinkViewSet(CommonViewSet):
    serializer_class = ResourceTypeLinkSerializer
    queryset = ResourceTypeLink.objects.all()


class ResourceTypesViewSet(CommonViewSet):
    serializer_class = ResourceTypesSerializer
    queryset = ResourceTypes.objects.all()


class ResourceValidationModeViewSet(CommonViewSet):
    serializer_class = ResourceValidationModeSerializer
    queryset = ResourceValidationMode.objects.all()


class ResponseCodeViewSet(CommonViewSet):
    serializer_class = ResponseCodeSerializer
    queryset = ResponseCode.objects.all()


class RestfulConformanceModeViewSet(CommonViewSet):
    serializer_class = RestfulConformanceModeSerializer
    queryset = RestfulConformanceMode.objects.all()


class RestfulInteractionViewSet(CommonViewSet):
    serializer_class = RestfulInteractionSerializer
    queryset = RestfulInteraction.objects.all()


class RestfulSecurityServiceViewSet(CommonViewSet):
    serializer_class = RestfulSecurityServiceSerializer
    queryset = RestfulSecurityService.objects.all()


class RiskProbabilityViewSet(CommonViewSet):
    serializer_class = RiskProbabilitySerializer
    queryset = RiskProbability.objects.all()


class RulesetViewSet(CommonViewSet):
    serializer_class = RulesetSerializer
    queryset = Ruleset.objects.all()


class SearchEntryModeViewSet(CommonViewSet):
    serializer_class = SearchEntryModeSerializer
    queryset = SearchEntryMode.objects.all()


class SearchModifierCodeViewSet(CommonViewSet):
    serializer_class = SearchModifierCodeSerializer
    queryset = SearchModifierCode.objects.all()


class SearchParamTypeViewSet(CommonViewSet):
    serializer_class = SearchParamTypeSerializer
    queryset = SearchParamType.objects.all()


class SearchXpathUsageViewSet(CommonViewSet):
    serializer_class = SearchXpathUsageSerializer
    queryset = SearchXpathUsage.objects.all()


class AuditSourceTypeViewSet(CommonViewSet):
    serializer_class = AuditSourceTypeSerializer
    queryset = AuditSourceType.objects.all()


class SelectionBehaviorViewSet(CommonViewSet):
    serializer_class = SelectionBehaviorSerializer
    queryset = SelectionBehavior.objects.all()


class SequenceTypeViewSet(CommonViewSet):
    serializer_class = SequenceTypeSerializer
    queryset = SequenceType.objects.all()


class ServiceCategoryViewSet(CommonViewSet):
    serializer_class = ServiceCategorySerializer
    queryset = ServiceCategory.objects.all()


class ServiceProvisionConditionsViewSet(CommonViewSet):
    serializer_class = ServiceProvisionConditionsSerializer
    queryset = ServiceProvisionConditions.objects.all()


class ServiceReferralMethodViewSet(CommonViewSet):
    serializer_class = ServiceReferralMethodSerializer
    queryset = ServiceReferralMethod.objects.all()


class ServiceTypeViewSet(CommonViewSet):
    serializer_class = ServiceTypeSerializer
    queryset = ServiceType.objects.all()


class Icd10ProceduresViewSet(CommonViewSet):
    serializer_class = Icd10ProceduresSerializer
    queryset = Icd10Procedures.objects.all()


class SlotstatusViewSet(CommonViewSet):
    serializer_class = SlotstatusSerializer
    queryset = Slotstatus.objects.all()


class SpecialValuesViewSet(CommonViewSet):
    serializer_class = SpecialValuesSerializer
    queryset = SpecialValues.objects.all()


class SpecimenStatusViewSet(CommonViewSet):
    serializer_class = SpecimenStatusSerializer
    queryset = SpecimenStatus.objects.all()


class StructureDefinitionKindViewSet(CommonViewSet):
    serializer_class = StructureDefinitionKindSerializer
    queryset = StructureDefinitionKind.objects.all()


class SubscriptionChannelTypeViewSet(CommonViewSet):
    serializer_class = SubscriptionChannelTypeSerializer
    queryset = SubscriptionChannelType.objects.all()


class SubscriptionStatusViewSet(CommonViewSet):
    serializer_class = SubscriptionStatusSerializer
    queryset = SubscriptionStatus.objects.all()


class SubscriptionTagViewSet(CommonViewSet):
    serializer_class = SubscriptionTagSerializer
    queryset = SubscriptionTag.objects.all()


class SubstanceCategoryViewSet(CommonViewSet):
    serializer_class = SubstanceCategorySerializer
    queryset = SubstanceCategory.objects.all()


class SupplydeliveryTypeViewSet(CommonViewSet):
    serializer_class = SupplydeliveryTypeSerializer
    queryset = SupplydeliveryType.objects.all()


class SupplyrequestKindViewSet(CommonViewSet):
    serializer_class = SupplyrequestKindSerializer
    queryset = SupplyrequestKind.objects.all()


class SupplydeliveryStatusViewSet(CommonViewSet):
    serializer_class = SupplydeliveryStatusSerializer
    queryset = SupplydeliveryStatus.objects.all()


class SupplyrequestReasonViewSet(CommonViewSet):
    serializer_class = SupplyrequestReasonSerializer
    queryset = SupplyrequestReason.objects.all()


class SupplyrequestStatusViewSet(CommonViewSet):
    serializer_class = SupplyrequestStatusSerializer
    queryset = SupplyrequestStatus.objects.all()


class TaskPerformerTypeViewSet(CommonViewSet):
    serializer_class = TaskPerformerTypeSerializer
    queryset = TaskPerformerType.objects.all()


class TaskPriorityViewSet(CommonViewSet):
    serializer_class = TaskPrioritySerializer
    queryset = TaskPriority.objects.all()


class TaskStageViewSet(CommonViewSet):
    serializer_class = TaskStageSerializer
    queryset = TaskStage.objects.all()


class TaskStatusViewSet(CommonViewSet):
    serializer_class = TaskStatusSerializer
    queryset = TaskStatus.objects.all()


class TestscriptOperationCodesViewSet(CommonViewSet):
    serializer_class = TestscriptOperationCodesSerializer
    queryset = TestscriptOperationCodes.objects.all()


class TestscriptProfileDestinationTypesViewSet(CommonViewSet):
    serializer_class = TestscriptProfileDestinationTypesSerializer
    queryset = TestscriptProfileDestinationTypes.objects.all()


class TestscriptProfileOriginTypesViewSet(CommonViewSet):
    serializer_class = TestscriptProfileOriginTypesSerializer
    queryset = TestscriptProfileOriginTypes.objects.all()


class TransactionModeViewSet(CommonViewSet):
    serializer_class = TransactionModeSerializer
    queryset = TransactionMode.objects.all()


class TriggerTypeViewSet(CommonViewSet):
    serializer_class = TriggerTypeSerializer
    queryset = TriggerType.objects.all()


class TypeDerivationRuleViewSet(CommonViewSet):
    serializer_class = TypeDerivationRuleSerializer
    queryset = TypeDerivationRule.objects.all()


class UnknownContentCodeViewSet(CommonViewSet):
    serializer_class = UnknownContentCodeSerializer
    queryset = UnknownContentCode.objects.all()


class VaccinationProtocolDoseStatusViewSet(CommonViewSet):
    serializer_class = VaccinationProtocolDoseStatusSerializer
    queryset = VaccinationProtocolDoseStatus.objects.all()


class VaccinationProtocolDoseStatusReasonViewSet(CommonViewSet):
    serializer_class = VaccinationProtocolDoseStatusReasonSerializer
    queryset = VaccinationProtocolDoseStatusReason.objects.all()


class VariantStateViewSet(CommonViewSet):
    serializer_class = VariantStateSerializer
    queryset = VariantState.objects.all()


class VersioningPolicyViewSet(CommonViewSet):
    serializer_class = VersioningPolicySerializer
    queryset = VersioningPolicy.objects.all()


class VisionBaseCodesViewSet(CommonViewSet):
    serializer_class = VisionBaseCodesSerializer
    queryset = VisionBaseCodes.objects.all()


class VisionEyeCodesViewSet(CommonViewSet):
    serializer_class = VisionEyeCodesSerializer
    queryset = VisionEyeCodes.objects.all()


class XdsRelationshipTypeViewSet(CommonViewSet):
    serializer_class = XdsRelationshipTypeSerializer
    queryset = XdsRelationshipType.objects.all()


class AcknowledgementconditionViewSet(CommonViewSet):
    serializer_class = AcknowledgementconditionSerializer
    queryset = Acknowledgementcondition.objects.all()


class AcknowledgementdetailcodeViewSet(CommonViewSet):
    serializer_class = AcknowledgementdetailcodeSerializer
    queryset = Acknowledgementdetailcode.objects.all()


class AcknowledgementdetailtypeViewSet(CommonViewSet):
    serializer_class = AcknowledgementdetailtypeSerializer
    queryset = Acknowledgementdetailtype.objects.all()


class AcknowledgementtypeViewSet(CommonViewSet):
    serializer_class = AcknowledgementtypeSerializer
    queryset = Acknowledgementtype.objects.all()


class ActclassViewSet(CommonViewSet):
    serializer_class = ActclassSerializer
    queryset = Actclass.objects.all()


class ActcodeViewSet(CommonViewSet):
    serializer_class = ActcodeSerializer
    queryset = Actcode.objects.all()


class ActexposurelevelcodeViewSet(CommonViewSet):
    serializer_class = ActexposurelevelcodeSerializer
    queryset = Actexposurelevelcode.objects.all()


class ActinvoiceelementmodifierViewSet(CommonViewSet):
    serializer_class = ActinvoiceelementmodifierSerializer
    queryset = Actinvoiceelementmodifier.objects.all()


class ActmoodViewSet(CommonViewSet):
    serializer_class = ActmoodSerializer
    queryset = Actmood.objects.all()


class ActpriorityViewSet(CommonViewSet):
    serializer_class = ActprioritySerializer
    queryset = Actpriority.objects.all()


class ActreasonViewSet(CommonViewSet):
    serializer_class = ActreasonSerializer
    queryset = Actreason.objects.all()


class ActrelationshipcheckpointViewSet(CommonViewSet):
    serializer_class = ActrelationshipcheckpointSerializer
    queryset = Actrelationshipcheckpoint.objects.all()


class ActrelationshipjoinViewSet(CommonViewSet):
    serializer_class = ActrelationshipjoinSerializer
    queryset = Actrelationshipjoin.objects.all()


class ActrelationshipsplitViewSet(CommonViewSet):
    serializer_class = ActrelationshipsplitSerializer
    queryset = Actrelationshipsplit.objects.all()


class ActrelationshipsubsetViewSet(CommonViewSet):
    serializer_class = ActrelationshipsubsetSerializer
    queryset = Actrelationshipsubset.objects.all()


class ActrelationshiptypeViewSet(CommonViewSet):
    serializer_class = ActrelationshiptypeSerializer
    queryset = Actrelationshiptype.objects.all()


class ActsiteViewSet(CommonViewSet):
    serializer_class = ActsiteSerializer
    queryset = Actsite.objects.all()


class ActstatusViewSet(CommonViewSet):
    serializer_class = ActstatusSerializer
    queryset = Actstatus.objects.all()


class ActusprivacylawViewSet(CommonViewSet):
    serializer_class = ActusprivacylawSerializer
    queryset = Actusprivacylaw.objects.all()


class ActuncertaintyViewSet(CommonViewSet):
    serializer_class = ActuncertaintySerializer
    queryset = Actuncertainty.objects.all()


class AddressparttypeViewSet(CommonViewSet):
    serializer_class = AddressparttypeSerializer
    queryset = Addressparttype.objects.all()


class AmericanindianalaskanativelanguagesViewSet(CommonViewSet):
    serializer_class = AmericanindianalaskanativelanguagesSerializer
    queryset = Americanindianalaskanativelanguages.objects.all()


class CalendarViewSet(CommonViewSet):
    serializer_class = CalendarSerializer
    queryset = Calendar.objects.all()


class CalendarcycleViewSet(CommonViewSet):
    serializer_class = CalendarcycleSerializer
    queryset = Calendarcycle.objects.all()


class CalendartypeViewSet(CommonViewSet):
    serializer_class = CalendartypeSerializer
    queryset = Calendartype.objects.all()


class CharsetViewSet(CommonViewSet):
    serializer_class = CharsetSerializer
    queryset = Charset.objects.all()


class CodingrationaleViewSet(CommonViewSet):
    serializer_class = CodingrationaleSerializer
    queryset = Codingrationale.objects.all()


class CommunicationfunctiontypeViewSet(CommonViewSet):
    serializer_class = CommunicationfunctiontypeSerializer
    queryset = Communicationfunctiontype.objects.all()


class CompressionalgorithmViewSet(CommonViewSet):
    serializer_class = CompressionalgorithmSerializer
    queryset = Compressionalgorithm.objects.all()


class ConfidentialityViewSet(CommonViewSet):
    serializer_class = ConfidentialitySerializer
    queryset = Confidentiality.objects.all()


class ContainercapViewSet(CommonViewSet):
    serializer_class = ContainercapSerializer
    queryset = Containercap.objects.all()


class ContainerseparatorViewSet(CommonViewSet):
    serializer_class = ContainerseparatorSerializer
    queryset = Containerseparator.objects.all()


class ContentprocessingmodeViewSet(CommonViewSet):
    serializer_class = ContentprocessingmodeSerializer
    queryset = Contentprocessingmode.objects.all()


class ContextcontrolViewSet(CommonViewSet):
    serializer_class = ContextcontrolSerializer
    queryset = Contextcontrol.objects.all()


class DataoperationViewSet(CommonViewSet):
    serializer_class = DataoperationSerializer
    queryset = Dataoperation.objects.all()


class DevicealertlevelViewSet(CommonViewSet):
    serializer_class = DevicealertlevelSerializer
    queryset = Devicealertlevel.objects.all()


class DocumentcompletionViewSet(CommonViewSet):
    serializer_class = DocumentcompletionSerializer
    queryset = Documentcompletion.objects.all()


class DocumentstorageViewSet(CommonViewSet):
    serializer_class = DocumentstorageSerializer
    queryset = Documentstorage.objects.all()


class EducationlevelViewSet(CommonViewSet):
    serializer_class = EducationlevelSerializer
    queryset = Educationlevel.objects.all()


class EmployeejobclassViewSet(CommonViewSet):
    serializer_class = EmployeejobclassSerializer
    queryset = Employeejobclass.objects.all()


class EncounteradmissionsourceViewSet(CommonViewSet):
    serializer_class = EncounteradmissionsourceSerializer
    queryset = Encounteradmissionsource.objects.all()


class EncounterspecialcourtesyViewSet(CommonViewSet):
    serializer_class = EncounterspecialcourtesySerializer
    queryset = Encounterspecialcourtesy.objects.all()


class EntityclassViewSet(CommonViewSet):
    serializer_class = EntityclassSerializer
    queryset = Entityclass.objects.all()


class EntitycodeViewSet(CommonViewSet):
    serializer_class = EntitycodeSerializer
    queryset = Entitycode.objects.all()


class EntitydeterminerViewSet(CommonViewSet):
    serializer_class = EntitydeterminerSerializer
    queryset = Entitydeterminer.objects.all()


class EntityhandlingViewSet(CommonViewSet):
    serializer_class = EntityhandlingSerializer
    queryset = Entityhandling.objects.all()


class EntitynamepartqualifierViewSet(CommonViewSet):
    serializer_class = EntitynamepartqualifierSerializer
    queryset = Entitynamepartqualifier.objects.all()


class Entitynamepartqualifierr2ViewSet(CommonViewSet):
    serializer_class = Entitynamepartqualifierr2Serializer
    queryset = Entitynamepartqualifierr2.objects.all()


class EntitynameparttypeViewSet(CommonViewSet):
    serializer_class = EntitynameparttypeSerializer
    queryset = Entitynameparttype.objects.all()


class Entitynameparttyper2ViewSet(CommonViewSet):
    serializer_class = Entitynameparttyper2Serializer
    queryset = Entitynameparttyper2.objects.all()


class EntitynameuseViewSet(CommonViewSet):
    serializer_class = EntitynameuseSerializer
    queryset = Entitynameuse.objects.all()


class Entitynameuser2ViewSet(CommonViewSet):
    serializer_class = Entitynameuser2Serializer
    queryset = Entitynameuser2.objects.all()


class EntityriskViewSet(CommonViewSet):
    serializer_class = EntityriskSerializer
    queryset = Entityrisk.objects.all()


class EntitystatusViewSet(CommonViewSet):
    serializer_class = EntitystatusSerializer
    queryset = Entitystatus.objects.all()


class EquipmentalertlevelViewSet(CommonViewSet):
    serializer_class = EquipmentalertlevelSerializer
    queryset = Equipmentalertlevel.objects.all()


class EthnicityViewSet(CommonViewSet):
    serializer_class = EthnicitySerializer
    queryset = Ethnicity.objects.all()


class ExposuremodeViewSet(CommonViewSet):
    serializer_class = ExposuremodeSerializer
    queryset = Exposuremode.objects.all()


class GtsabbreviationViewSet(CommonViewSet):
    serializer_class = GtsabbreviationSerializer
    queryset = Gtsabbreviation.objects.all()


class GenderstatusViewSet(CommonViewSet):
    serializer_class = GenderstatusSerializer
    queryset = Genderstatus.objects.all()


class Hl7updatemodeViewSet(CommonViewSet):
    serializer_class = Hl7updatemodeSerializer
    queryset = Hl7updatemode.objects.all()


class HtmllinktypeViewSet(CommonViewSet):
    serializer_class = HtmllinktypeSerializer
    queryset = Htmllinktype.objects.all()


class IdentifierreliabilityViewSet(CommonViewSet):
    serializer_class = IdentifierreliabilitySerializer
    queryset = Identifierreliability.objects.all()


class IdentifierscopeViewSet(CommonViewSet):
    serializer_class = IdentifierscopeSerializer
    queryset = Identifierscope.objects.all()


class IntegritycheckalgorithmViewSet(CommonViewSet):
    serializer_class = IntegritycheckalgorithmSerializer
    queryset = Integritycheckalgorithm.objects.all()


class LanguageabilitymodeViewSet(CommonViewSet):
    serializer_class = LanguageabilitymodeSerializer
    queryset = Languageabilitymode.objects.all()


class LanguageabilityproficiencyViewSet(CommonViewSet):
    serializer_class = LanguageabilityproficiencySerializer
    queryset = Languageabilityproficiency.objects.all()


class LivingarrangementViewSet(CommonViewSet):
    serializer_class = LivingarrangementSerializer
    queryset = Livingarrangement.objects.all()


class LocalmarkupignoreViewSet(CommonViewSet):
    serializer_class = LocalmarkupignoreSerializer
    queryset = Localmarkupignore.objects.all()


class LocalremotecontrolstateViewSet(CommonViewSet):
    serializer_class = LocalremotecontrolstateSerializer
    queryset = Localremotecontrolstate.objects.all()


class ManagedparticipationstatusViewSet(CommonViewSet):
    serializer_class = ManagedparticipationstatusSerializer
    queryset = Managedparticipationstatus.objects.all()


class MaprelationshipViewSet(CommonViewSet):
    serializer_class = MaprelationshipSerializer
    queryset = Maprelationship.objects.all()


class MessagewaitingpriorityViewSet(CommonViewSet):
    serializer_class = MessagewaitingprioritySerializer
    queryset = Messagewaitingpriority.objects.all()


class ModifyindicatorViewSet(CommonViewSet):
    serializer_class = ModifyindicatorSerializer
    queryset = Modifyindicator.objects.all()


class NullflavorViewSet(CommonViewSet):
    serializer_class = NullflavorSerializer
    queryset = Nullflavor.objects.all()


class ObservationinterpretationViewSet(CommonViewSet):
    serializer_class = ObservationinterpretationSerializer
    queryset = Observationinterpretation.objects.all()


class ObservationmethodViewSet(CommonViewSet):
    serializer_class = ObservationmethodSerializer
    queryset = Observationmethod.objects.all()


class ObservationvalueViewSet(CommonViewSet):
    serializer_class = ObservationvalueSerializer
    queryset = Observationvalue.objects.all()


class ParticipationfunctionViewSet(CommonViewSet):
    serializer_class = ParticipationfunctionSerializer
    queryset = Participationfunction.objects.all()


class ParticipationmodeViewSet(CommonViewSet):
    serializer_class = ParticipationmodeSerializer
    queryset = Participationmode.objects.all()


class ParticipationsignatureViewSet(CommonViewSet):
    serializer_class = ParticipationsignatureSerializer
    queryset = Participationsignature.objects.all()


class ParticipationtypeViewSet(CommonViewSet):
    serializer_class = ParticipationtypeSerializer
    queryset = Participationtype.objects.all()


class PatientimportanceViewSet(CommonViewSet):
    serializer_class = PatientimportanceSerializer
    queryset = Patientimportance.objects.all()


class PaymenttermsViewSet(CommonViewSet):
    serializer_class = PaymenttermsSerializer
    queryset = Paymentterms.objects.all()


class PersondisabilitytypeViewSet(CommonViewSet):
    serializer_class = PersondisabilitytypeSerializer
    queryset = Persondisabilitytype.objects.all()


class ProbabilitydistributiontypeViewSet(CommonViewSet):
    serializer_class = ProbabilitydistributiontypeSerializer
    queryset = Probabilitydistributiontype.objects.all()


class ProcessingidViewSet(CommonViewSet):
    serializer_class = ProcessingidSerializer
    queryset = Processingid.objects.all()


class ProcessingmodeViewSet(CommonViewSet):
    serializer_class = ProcessingmodeSerializer
    queryset = Processingmode.objects.all()


class QueryparametervalueViewSet(CommonViewSet):
    serializer_class = QueryparametervalueSerializer
    queryset = Queryparametervalue.objects.all()


class QuerypriorityViewSet(CommonViewSet):
    serializer_class = QueryprioritySerializer
    queryset = Querypriority.objects.all()


class QueryrequestlimitViewSet(CommonViewSet):
    serializer_class = QueryrequestlimitSerializer
    queryset = Queryrequestlimit.objects.all()


class QueryresponseViewSet(CommonViewSet):
    serializer_class = QueryresponseSerializer
    queryset = Queryresponse.objects.all()


class QuerystatuscodeViewSet(CommonViewSet):
    serializer_class = QuerystatuscodeSerializer
    queryset = Querystatuscode.objects.all()


class RaceViewSet(CommonViewSet):
    serializer_class = RaceSerializer
    queryset = Race.objects.all()


class RelationaloperatorViewSet(CommonViewSet):
    serializer_class = RelationaloperatorSerializer
    queryset = Relationaloperator.objects.all()


class RelationshipconjunctionViewSet(CommonViewSet):
    serializer_class = RelationshipconjunctionSerializer
    queryset = Relationshipconjunction.objects.all()


class ReligiousaffiliationViewSet(CommonViewSet):
    serializer_class = ReligiousaffiliationSerializer
    queryset = Religiousaffiliation.objects.all()


class ResponselevelViewSet(CommonViewSet):
    serializer_class = ResponselevelSerializer
    queryset = Responselevel.objects.all()


class ResponsemodalityViewSet(CommonViewSet):
    serializer_class = ResponsemodalitySerializer
    queryset = Responsemodality.objects.all()


class ResponsemodeViewSet(CommonViewSet):
    serializer_class = ResponsemodeSerializer
    queryset = Responsemode.objects.all()


class RoleclassViewSet(CommonViewSet):
    serializer_class = RoleclassSerializer
    queryset = Roleclass.objects.all()


class RolecodeViewSet(CommonViewSet):
    serializer_class = RolecodeSerializer
    queryset = Rolecode.objects.all()


class RolelinkstatusViewSet(CommonViewSet):
    serializer_class = RolelinkstatusSerializer
    queryset = Rolelinkstatus.objects.all()


class RolelinktypeViewSet(CommonViewSet):
    serializer_class = RolelinktypeSerializer
    queryset = Rolelinktype.objects.all()


class RolestatusViewSet(CommonViewSet):
    serializer_class = RolestatusSerializer
    queryset = Rolestatus.objects.all()


class RouteofadministrationViewSet(CommonViewSet):
    serializer_class = RouteofadministrationSerializer
    queryset = Routeofadministration.objects.all()


class SequencingViewSet(CommonViewSet):
    serializer_class = SequencingSerializer
    queryset = Sequencing.objects.all()


class SetoperatorViewSet(CommonViewSet):
    serializer_class = SetoperatorSerializer
    queryset = Setoperator.objects.all()


class SpecimentypeViewSet(CommonViewSet):
    serializer_class = SpecimentypeSerializer
    queryset = Specimentype.objects.all()


class SubstitutionconditionViewSet(CommonViewSet):
    serializer_class = SubstitutionconditionSerializer
    queryset = Substitutioncondition.objects.all()


class TablecellhorizontalalignViewSet(CommonViewSet):
    serializer_class = TablecellhorizontalalignSerializer
    queryset = Tablecellhorizontalalign.objects.all()


class TablecellscopeViewSet(CommonViewSet):
    serializer_class = TablecellscopeSerializer
    queryset = Tablecellscope.objects.all()


class TablecellverticalalignViewSet(CommonViewSet):
    serializer_class = TablecellverticalalignSerializer
    queryset = Tablecellverticalalign.objects.all()


class TableframeViewSet(CommonViewSet):
    serializer_class = TableframeSerializer
    queryset = Tableframe.objects.all()


class TablerulesViewSet(CommonViewSet):
    serializer_class = TablerulesSerializer
    queryset = Tablerules.objects.all()


class TargetawarenessViewSet(CommonViewSet):
    serializer_class = TargetawarenessSerializer
    queryset = Targetawareness.objects.all()


class TelecommunicationcapabilitiesViewSet(CommonViewSet):
    serializer_class = TelecommunicationcapabilitiesSerializer
    queryset = Telecommunicationcapabilities.objects.all()


class TimingeventViewSet(CommonViewSet):
    serializer_class = TimingeventSerializer
    queryset = Timingevent.objects.all()


class TransmissionrelationshiptypecodeViewSet(CommonViewSet):
    serializer_class = TransmissionrelationshiptypecodeSerializer
    queryset = Transmissionrelationshiptypecode.objects.all()


class TribalentityusViewSet(CommonViewSet):
    serializer_class = TribalentityusSerializer
    queryset = Tribalentityus.objects.all()


class VaccinemanufacturerViewSet(CommonViewSet):
    serializer_class = VaccinemanufacturerSerializer
    queryset = Vaccinemanufacturer.objects.all()


class Hl7realmViewSet(CommonViewSet):
    serializer_class = Hl7realmSerializer
    queryset = Hl7realm.objects.all()


class Hl7v3conformanceViewSet(CommonViewSet):
    serializer_class = Hl7v3conformanceSerializer
    queryset = Hl7v3conformance.objects.all()


class OrderabledrugformViewSet(CommonViewSet):
    serializer_class = OrderabledrugformSerializer
    queryset = Orderabledrugform.objects.all()


class SubstanceadminsubstitutionViewSet(CommonViewSet):
    serializer_class = SubstanceadminsubstitutionSerializer
    queryset = Substanceadminsubstitution.objects.all()
