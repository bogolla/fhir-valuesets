from django.test import TestCase
from model_mommy import mommy

from fhir_valuesets.valuesets.models import *  # noqa


class TestExample(TestCase):
    def test_unicode(self):
        display = 'Example'
        data = mommy.make(Example, display=display)
        assert str(data) == display


class TestSurface(TestCase):
    def test_unicode(self):
        display = 'Surface'
        data = mommy.make(Surface, display=display)
        assert str(data) == display


class TestLoinc480020Answerlist(TestCase):
    def test_unicode(self):
        display = 'Loinc480020Answerlist'
        data = mommy.make(Loinc480020Answerlist, display=display)
        assert str(data) == display


class TestLoinc480194Answerlist(TestCase):
    def test_unicode(self):
        display = 'Loinc480194Answerlist'
        data = mommy.make(Loinc480194Answerlist, display=display)
        assert str(data) == display


class TestLoinc530345Answerlist(TestCase):
    def test_unicode(self):
        display = 'Loinc530345Answerlist'
        data = mommy.make(Loinc530345Answerlist, display=display)
        assert str(data) == display


class TestAbstractTypes(TestCase):
    def test_unicode(self):
        display = 'AbstractTypes'
        data = mommy.make(AbstractTypes, display=display)
        assert str(data) == display


class TestAccountStatus(TestCase):
    def test_unicode(self):
        display = 'AccountStatus'
        data = mommy.make(AccountStatus, display=display)
        assert str(data) == display


class TestActionBehaviorType(TestCase):
    def test_unicode(self):
        display = 'ActionBehaviorType'
        data = mommy.make(ActionBehaviorType, display=display)
        assert str(data) == display


class TestActionCardinalityBehavior(TestCase):
    def test_unicode(self):
        display = 'ActionCardinalityBehavior'
        data = mommy.make(ActionCardinalityBehavior, display=display)
        assert str(data) == display


class TestActionGroupingBehavior(TestCase):
    def test_unicode(self):
        display = 'ActionGroupingBehavior'
        data = mommy.make(ActionGroupingBehavior, display=display)
        assert str(data) == display


class TestActionParticipantType(TestCase):
    def test_unicode(self):
        display = 'ActionParticipantType'
        data = mommy.make(ActionParticipantType, display=display)
        assert str(data) == display


class TestActionPrecheckBehavior(TestCase):
    def test_unicode(self):
        display = 'ActionPrecheckBehavior'
        data = mommy.make(ActionPrecheckBehavior, display=display)
        assert str(data) == display


class TestActionRelationshipAnchor(TestCase):
    def test_unicode(self):
        display = 'ActionRelationshipAnchor'
        data = mommy.make(ActionRelationshipAnchor, display=display)
        assert str(data) == display


class TestActionRelationshipType(TestCase):
    def test_unicode(self):
        display = 'ActionRelationshipType'
        data = mommy.make(ActionRelationshipType, display=display)
        assert str(data) == display


class TestActionRequiredBehavior(TestCase):
    def test_unicode(self):
        display = 'ActionRequiredBehavior'
        data = mommy.make(ActionRequiredBehavior, display=display)
        assert str(data) == display


class TestActionSelectionBehavior(TestCase):
    def test_unicode(self):
        display = 'ActionSelectionBehavior'
        data = mommy.make(ActionSelectionBehavior, display=display)
        assert str(data) == display


class TestActionType(TestCase):
    def test_unicode(self):
        display = 'ActionType'
        data = mommy.make(ActionType, display=display)
        assert str(data) == display


class TestActionlist(TestCase):
    def test_unicode(self):
        display = 'Actionlist'
        data = mommy.make(Actionlist, display=display)
        assert str(data) == display


class TestActivityDefinitionCategory(TestCase):
    def test_unicode(self):
        display = 'ActivityDefinitionCategory'
        data = mommy.make(ActivityDefinitionCategory, display=display)
        assert str(data) == display


class TestActivityParticipantType(TestCase):
    def test_unicode(self):
        display = 'ActivityParticipantType'
        data = mommy.make(ActivityParticipantType, display=display)
        assert str(data) == display


class TestAdditionalmaterials(TestCase):
    def test_unicode(self):
        display = 'Additionalmaterials'
        data = mommy.make(Additionalmaterials, display=display)
        assert str(data) == display


class TestAddressType(TestCase):
    def test_unicode(self):
        display = 'AddressType'
        data = mommy.make(AddressType, display=display)
        assert str(data) == display


class TestAddressUse(TestCase):
    def test_unicode(self):
        display = 'AddressUse'
        data = mommy.make(AddressUse, display=display)
        assert str(data) == display


class TestAdjudication(TestCase):
    def test_unicode(self):
        display = 'Adjudication'
        data = mommy.make(Adjudication, display=display)
        assert str(data) == display


class TestAdjudicationError(TestCase):
    def test_unicode(self):
        display = 'AdjudicationError'
        data = mommy.make(AdjudicationError, display=display)
        assert str(data) == display


class TestAdjudicationReason(TestCase):
    def test_unicode(self):
        display = 'AdjudicationReason'
        data = mommy.make(AdjudicationReason, display=display)
        assert str(data) == display


class TestAdministrativeGender(TestCase):
    def test_unicode(self):
        display = 'AdministrativeGender'
        data = mommy.make(AdministrativeGender, display=display)
        assert str(data) == display


class TestEncounterAdmitSource(TestCase):
    def test_unicode(self):
        display = 'EncounterAdmitSource'
        data = mommy.make(EncounterAdmitSource, display=display)
        assert str(data) == display


class TestAllergyIntoleranceCategory(TestCase):
    def test_unicode(self):
        display = 'AllergyIntoleranceCategory'
        data = mommy.make(AllergyIntoleranceCategory, display=display)
        assert str(data) == display


class TestAllergyIntoleranceCriticality(TestCase):
    def test_unicode(self):
        display = 'AllergyIntoleranceCriticality'
        data = mommy.make(AllergyIntoleranceCriticality, display=display)
        assert str(data) == display


class TestAllergyIntoleranceStatus(TestCase):
    def test_unicode(self):
        display = 'AllergyIntoleranceStatus'
        data = mommy.make(AllergyIntoleranceStatus, display=display)
        assert str(data) == display


class TestAllergyIntoleranceType(TestCase):
    def test_unicode(self):
        display = 'AllergyIntoleranceType'
        data = mommy.make(AllergyIntoleranceType, display=display)
        assert str(data) == display


class TestAnimalBreeds(TestCase):
    def test_unicode(self):
        display = 'AnimalBreeds'
        data = mommy.make(AnimalBreeds, display=display)
        assert str(data) == display


class TestAnimalGenderstatus(TestCase):
    def test_unicode(self):
        display = 'AnimalGenderstatus'
        data = mommy.make(AnimalGenderstatus, display=display)
        assert str(data) == display


class TestAnimalSpecies(TestCase):
    def test_unicode(self):
        display = 'AnimalSpecies'
        data = mommy.make(AnimalSpecies, display=display)
        assert str(data) == display


class TestAppointmentstatus(TestCase):
    def test_unicode(self):
        display = 'Appointmentstatus'
        data = mommy.make(Appointmentstatus, display=display)
        assert str(data) == display


class TestAssertDirectionCodes(TestCase):
    def test_unicode(self):
        display = 'AssertDirectionCodes'
        data = mommy.make(AssertDirectionCodes, display=display)
        assert str(data) == display


class TestAssertOperatorCodes(TestCase):
    def test_unicode(self):
        display = 'AssertOperatorCodes'
        data = mommy.make(AssertOperatorCodes, display=display)
        assert str(data) == display


class TestAssertResponseCodeTypes(TestCase):
    def test_unicode(self):
        display = 'AssertResponseCodeTypes'
        data = mommy.make(AssertResponseCodeTypes, display=display)
        assert str(data) == display


class TestAuditEventAction(TestCase):
    def test_unicode(self):
        display = 'AuditEventAction'
        data = mommy.make(AuditEventAction, display=display)
        assert str(data) == display


class TestAuditEventOutcome(TestCase):
    def test_unicode(self):
        display = 'AuditEventOutcome'
        data = mommy.make(AuditEventOutcome, display=display)
        assert str(data) == display


class TestAuditEventType(TestCase):
    def test_unicode(self):
        display = 'AuditEventType'
        data = mommy.make(AuditEventType, display=display)
        assert str(data) == display


class TestBasicResourceType(TestCase):
    def test_unicode(self):
        display = 'BasicResourceType'
        data = mommy.make(BasicResourceType, display=display)
        assert str(data) == display


class TestBenefitCategory(TestCase):
    def test_unicode(self):
        display = 'BenefitCategory'
        data = mommy.make(BenefitCategory, display=display)
        assert str(data) == display


class TestBenefitNetwork(TestCase):
    def test_unicode(self):
        display = 'BenefitNetwork'
        data = mommy.make(BenefitNetwork, display=display)
        assert str(data) == display


class TestBenefitSubcategory(TestCase):
    def test_unicode(self):
        display = 'BenefitSubcategory'
        data = mommy.make(BenefitSubcategory, display=display)
        assert str(data) == display


class TestBenefitTerm(TestCase):
    def test_unicode(self):
        display = 'BenefitTerm'
        data = mommy.make(BenefitTerm, display=display)
        assert str(data) == display


class TestBenefitType(TestCase):
    def test_unicode(self):
        display = 'BenefitType'
        data = mommy.make(BenefitType, display=display)
        assert str(data) == display


class TestBenefitUnit(TestCase):
    def test_unicode(self):
        display = 'BenefitUnit'
        data = mommy.make(BenefitUnit, display=display)
        assert str(data) == display


class TestBindingStrength(TestCase):
    def test_unicode(self):
        display = 'BindingStrength'
        data = mommy.make(BindingStrength, display=display)
        assert str(data) == display


class TestBundleType(TestCase):
    def test_unicode(self):
        display = 'BundleType'
        data = mommy.make(BundleType, display=display)
        assert str(data) == display


class TestCardinalityBehavior(TestCase):
    def test_unicode(self):
        display = 'CardinalityBehavior'
        data = mommy.make(CardinalityBehavior, display=display)
        assert str(data) == display


class TestCarePlanActivityCategory(TestCase):
    def test_unicode(self):
        display = 'CarePlanActivityCategory'
        data = mommy.make(CarePlanActivityCategory, display=display)
        assert str(data) == display


class TestCarePlanActivityStatus(TestCase):
    def test_unicode(self):
        display = 'CarePlanActivityStatus'
        data = mommy.make(CarePlanActivityStatus, display=display)
        assert str(data) == display


class TestCarePlanRelationship(TestCase):
    def test_unicode(self):
        display = 'CarePlanRelationship'
        data = mommy.make(CarePlanRelationship, display=display)
        assert str(data) == display


class TestCarePlanStatus(TestCase):
    def test_unicode(self):
        display = 'CarePlanStatus'
        data = mommy.make(CarePlanStatus, display=display)
        assert str(data) == display


class TestCdsRuleActionType(TestCase):
    def test_unicode(self):
        display = 'CdsRuleActionType'
        data = mommy.make(CdsRuleActionType, display=display)
        assert str(data) == display


class TestCdsRuleParticipant(TestCase):
    def test_unicode(self):
        display = 'CdsRuleParticipant'
        data = mommy.make(CdsRuleParticipant, display=display)
        assert str(data) == display


class TestCdsRuleTriggerType(TestCase):
    def test_unicode(self):
        display = 'CdsRuleTriggerType'
        data = mommy.make(CdsRuleTriggerType, display=display)
        assert str(data) == display


class TestChoiceListOrientation(TestCase):
    def test_unicode(self):
        display = 'ChoiceListOrientation'
        data = mommy.make(ChoiceListOrientation, display=display)
        assert str(data) == display


class TestChromosomeHuman(TestCase):
    def test_unicode(self):
        display = 'ChromosomeHuman'
        data = mommy.make(ChromosomeHuman, display=display)
        assert str(data) == display


class TestClaimException(TestCase):
    def test_unicode(self):
        display = 'ClaimException'
        data = mommy.make(ClaimException, display=display)
        assert str(data) == display


class TestClaimTypeLink(TestCase):
    def test_unicode(self):
        display = 'ClaimTypeLink'
        data = mommy.make(ClaimTypeLink, display=display)
        assert str(data) == display


class TestClaimTypeLink2(TestCase):
    def test_unicode(self):
        display = 'ClaimTypeLink2'
        data = mommy.make(ClaimTypeLink2, display=display)
        assert str(data) == display


class TestClaimUseLink(TestCase):
    def test_unicode(self):
        display = 'ClaimUseLink'
        data = mommy.make(ClaimUseLink, display=display)
        assert str(data) == display


class TestClaimCareteamrole(TestCase):
    def test_unicode(self):
        display = 'ClaimCareteamrole'
        data = mommy.make(ClaimCareteamrole, display=display)
        assert str(data) == display


class TestClaimInformationcategory(TestCase):
    def test_unicode(self):
        display = 'ClaimInformationcategory'
        data = mommy.make(ClaimInformationcategory, display=display)
        assert str(data) == display


class TestClassificationOrContext(TestCase):
    def test_unicode(self):
        display = 'ClassificationOrContext'
        data = mommy.make(ClassificationOrContext, display=display)
        assert str(data) == display


class TestClinicalImpressionStatus(TestCase):
    def test_unicode(self):
        display = 'ClinicalImpressionStatus'
        data = mommy.make(ClinicalImpressionStatus, display=display)
        assert str(data) == display


class TestContentMode(TestCase):
    def test_unicode(self):
        display = 'ContentMode'
        data = mommy.make(ContentMode, display=display)
        assert str(data) == display


class TestCommunicationRequestStatus(TestCase):
    def test_unicode(self):
        display = 'CommunicationRequestStatus'
        data = mommy.make(CommunicationRequestStatus, display=display)
        assert str(data) == display


class TestCommunicationStatus(TestCase):
    def test_unicode(self):
        display = 'CommunicationStatus'
        data = mommy.make(CommunicationStatus, display=display)
        assert str(data) == display


class TestCompartmentType(TestCase):
    def test_unicode(self):
        display = 'CompartmentType'
        data = mommy.make(CompartmentType, display=display)
        assert str(data) == display


class TestCompositionAttestationMode(TestCase):
    def test_unicode(self):
        display = 'CompositionAttestationMode'
        data = mommy.make(CompositionAttestationMode, display=display)
        assert str(data) == display


class TestCompositionStatus(TestCase):
    def test_unicode(self):
        display = 'CompositionStatus'
        data = mommy.make(CompositionStatus, display=display)
        assert str(data) == display


class TestConceptMapEquivalence(TestCase):
    def test_unicode(self):
        display = 'ConceptMapEquivalence'
        data = mommy.make(ConceptMapEquivalence, display=display)
        assert str(data) == display


class TestConceptProperties(TestCase):
    def test_unicode(self):
        display = 'ConceptProperties'
        data = mommy.make(ConceptProperties, display=display)
        assert str(data) == display


class TestConceptPropertyType(TestCase):
    def test_unicode(self):
        display = 'ConceptPropertyType'
        data = mommy.make(ConceptPropertyType, display=display)
        assert str(data) == display


class TestConditionCategory(TestCase):
    def test_unicode(self):
        display = 'ConditionCategory'
        data = mommy.make(ConditionCategory, display=display)
        assert str(data) == display


class TestConditionClinical(TestCase):
    def test_unicode(self):
        display = 'ConditionClinical'
        data = mommy.make(ConditionClinical, display=display)
        assert str(data) == display


class TestConditionState(TestCase):
    def test_unicode(self):
        display = 'ConditionState'
        data = mommy.make(ConditionState, display=display)
        assert str(data) == display


class TestConditionVerStatus(TestCase):
    def test_unicode(self):
        display = 'ConditionVerStatus'
        data = mommy.make(ConditionVerStatus, display=display)
        assert str(data) == display


class TestConditionalDeleteStatus(TestCase):
    def test_unicode(self):
        display = 'ConditionalDeleteStatus'
        data = mommy.make(ConditionalDeleteStatus, display=display)
        assert str(data) == display


class TestConformanceExpectation(TestCase):
    def test_unicode(self):
        display = 'ConformanceExpectation'
        data = mommy.make(ConformanceExpectation, display=display)
        assert str(data) == display


class TestConformanceResourceStatus(TestCase):
    def test_unicode(self):
        display = 'ConformanceResourceStatus'
        data = mommy.make(ConformanceResourceStatus, display=display)
        assert str(data) == display


class TestConformanceStatementKind(TestCase):
    def test_unicode(self):
        display = 'ConformanceStatementKind'
        data = mommy.make(ConformanceStatementKind, display=display)
        assert str(data) == display


class TestConsentDataMeaning(TestCase):
    def test_unicode(self):
        display = 'ConsentDataMeaning'
        data = mommy.make(ConsentDataMeaning, display=display)
        assert str(data) == display


class TestConsentExceptType(TestCase):
    def test_unicode(self):
        display = 'ConsentExceptType'
        data = mommy.make(ConsentExceptType, display=display)
        assert str(data) == display


class TestConsentStatus(TestCase):
    def test_unicode(self):
        display = 'ConsentStatus'
        data = mommy.make(ConsentStatus, display=display)
        assert str(data) == display


class TestConsentAction(TestCase):
    def test_unicode(self):
        display = 'ConsentAction'
        data = mommy.make(ConsentAction, display=display)
        assert str(data) == display


class TestConsentCategory(TestCase):
    def test_unicode(self):
        display = 'ConsentCategory'
        data = mommy.make(ConsentCategory, display=display)
        assert str(data) == display


class TestConstraintSeverity(TestCase):
    def test_unicode(self):
        display = 'ConstraintSeverity'
        data = mommy.make(ConstraintSeverity, display=display)
        assert str(data) == display


class TestContactPointSystem(TestCase):
    def test_unicode(self):
        display = 'ContactPointSystem'
        data = mommy.make(ContactPointSystem, display=display)
        assert str(data) == display


class TestContactPointUse(TestCase):
    def test_unicode(self):
        display = 'ContactPointUse'
        data = mommy.make(ContactPointUse, display=display)
        assert str(data) == display


class TestContactentityType(TestCase):
    def test_unicode(self):
        display = 'ContactentityType'
        data = mommy.make(ContactentityType, display=display)
        assert str(data) == display


class TestContentType(TestCase):
    def test_unicode(self):
        display = 'ContentType'
        data = mommy.make(ContentType, display=display)
        assert str(data) == display


class TestContractSubtype(TestCase):
    def test_unicode(self):
        display = 'ContractSubtype'
        data = mommy.make(ContractSubtype, display=display)
        assert str(data) == display


class TestContractTermSubtype(TestCase):
    def test_unicode(self):
        display = 'ContractTermSubtype'
        data = mommy.make(ContractTermSubtype, display=display)
        assert str(data) == display


class TestContractTermType(TestCase):
    def test_unicode(self):
        display = 'ContractTermType'
        data = mommy.make(ContractTermType, display=display)
        assert str(data) == display


class TestContractType(TestCase):
    def test_unicode(self):
        display = 'ContractType'
        data = mommy.make(ContractType, display=display)
        assert str(data) == display


class TestCopyNumberEvent(TestCase):
    def test_unicode(self):
        display = 'CopyNumberEvent'
        data = mommy.make(CopyNumberEvent, display=display)
        assert str(data) == display


class TestCoverageException(TestCase):
    def test_unicode(self):
        display = 'CoverageException'
        data = mommy.make(CoverageException, display=display)
        assert str(data) == display


class TestDwebtype(TestCase):
    def test_unicode(self):
        display = 'Dwebtype'
        data = mommy.make(Dwebtype, display=display)
        assert str(data) == display


class TestDataAbsentReason(TestCase):
    def test_unicode(self):
        display = 'DataAbsentReason'
        data = mommy.make(DataAbsentReason, display=display)
        assert str(data) == display


class TestDataTypes(TestCase):
    def test_unicode(self):
        display = 'DataTypes'
        data = mommy.make(DataTypes, display=display)
        assert str(data) == display


class TestDataelementStringency(TestCase):
    def test_unicode(self):
        display = 'DataelementStringency'
        data = mommy.make(DataelementStringency, display=display)
        assert str(data) == display


class TestDaysOfWeek(TestCase):
    def test_unicode(self):
        display = 'DaysOfWeek'
        data = mommy.make(DaysOfWeek, display=display)
        assert str(data) == display


class TestDetectedissueSeverity(TestCase):
    def test_unicode(self):
        display = 'DetectedissueSeverity'
        data = mommy.make(DetectedissueSeverity, display=display)
        assert str(data) == display


class TestDeviceAction(TestCase):
    def test_unicode(self):
        display = 'DeviceAction'
        data = mommy.make(DeviceAction, display=display)
        assert str(data) == display


class TestDeviceUseRequestPriority(TestCase):
    def test_unicode(self):
        display = 'DeviceUseRequestPriority'
        data = mommy.make(DeviceUseRequestPriority, display=display)
        assert str(data) == display


class TestDeviceUseRequestStatus(TestCase):
    def test_unicode(self):
        display = 'DeviceUseRequestStatus'
        data = mommy.make(DeviceUseRequestStatus, display=display)
        assert str(data) == display


class TestDevicestatus(TestCase):
    def test_unicode(self):
        display = 'Devicestatus'
        data = mommy.make(Devicestatus, display=display)
        assert str(data) == display


class TestDiagnosticOrderPriority(TestCase):
    def test_unicode(self):
        display = 'DiagnosticOrderPriority'
        data = mommy.make(DiagnosticOrderPriority, display=display)
        assert str(data) == display


class TestDiagnosticOrderStatus(TestCase):
    def test_unicode(self):
        display = 'DiagnosticOrderStatus'
        data = mommy.make(DiagnosticOrderStatus, display=display)
        assert str(data) == display


class TestDiagnosticReportStatus(TestCase):
    def test_unicode(self):
        display = 'DiagnosticReportStatus'
        data = mommy.make(DiagnosticReportStatus, display=display)
        assert str(data) == display


class TestEncounterDiet(TestCase):
    def test_unicode(self):
        display = 'EncounterDiet'
        data = mommy.make(EncounterDiet, display=display)
        assert str(data) == display


class TestDigitalMediaType(TestCase):
    def test_unicode(self):
        display = 'DigitalMediaType'
        data = mommy.make(DigitalMediaType, display=display)
        assert str(data) == display


class TestEncounterDischargeDisposition(TestCase):
    def test_unicode(self):
        display = 'EncounterDischargeDisposition'
        data = mommy.make(EncounterDischargeDisposition, display=display)
        assert str(data) == display


class TestDocumentMode(TestCase):
    def test_unicode(self):
        display = 'DocumentMode'
        data = mommy.make(DocumentMode, display=display)
        assert str(data) == display


class TestDocumentReferenceStatus(TestCase):
    def test_unicode(self):
        display = 'DocumentReferenceStatus'
        data = mommy.make(DocumentReferenceStatus, display=display)
        assert str(data) == display


class TestDocumentRelationshipType(TestCase):
    def test_unicode(self):
        display = 'DocumentRelationshipType'
        data = mommy.make(DocumentRelationshipType, display=display)
        assert str(data) == display


class TestEncounterLocationStatus(TestCase):
    def test_unicode(self):
        display = 'EncounterLocationStatus'
        data = mommy.make(EncounterLocationStatus, display=display)
        assert str(data) == display


class TestEncounterPriority(TestCase):
    def test_unicode(self):
        display = 'EncounterPriority'
        data = mommy.make(EncounterPriority, display=display)
        assert str(data) == display


class TestEncounterSpecialArrangements(TestCase):
    def test_unicode(self):
        display = 'EncounterSpecialArrangements'
        data = mommy.make(EncounterSpecialArrangements, display=display)
        assert str(data) == display


class TestEncounterState(TestCase):
    def test_unicode(self):
        display = 'EncounterState'
        data = mommy.make(EncounterState, display=display)
        assert str(data) == display


class TestEncounterType(TestCase):
    def test_unicode(self):
        display = 'EncounterType'
        data = mommy.make(EncounterType, display=display)
        assert str(data) == display


class TestEndpointStatus(TestCase):
    def test_unicode(self):
        display = 'EndpointStatus'
        data = mommy.make(EndpointStatus, display=display)
        assert str(data) == display


class TestEntformulaAdditive(TestCase):
    def test_unicode(self):
        display = 'EntformulaAdditive'
        data = mommy.make(EntformulaAdditive, display=display)
        assert str(data) == display


class TestEpisodeOfCareStatus(TestCase):
    def test_unicode(self):
        display = 'EpisodeOfCareStatus'
        data = mommy.make(EpisodeOfCareStatus, display=display)
        assert str(data) == display


class TestServiceUscls(TestCase):
    def test_unicode(self):
        display = 'ServiceUscls'
        data = mommy.make(ServiceUscls, display=display)
        assert str(data) == display


class TestFmItemtype(TestCase):
    def test_unicode(self):
        display = 'FmItemtype'
        data = mommy.make(FmItemtype, display=display)
        assert str(data) == display


class TestOccurrenceCodes(TestCase):
    def test_unicode(self):
        display = 'OccurrenceCodes'
        data = mommy.make(OccurrenceCodes, display=display)
        assert str(data) == display


class TestOccurrenceSpanCodes(TestCase):
    def test_unicode(self):
        display = 'OccurrenceSpanCodes'
        data = mommy.make(OccurrenceSpanCodes, display=display)
        assert str(data) == display


class TestClaimSubtype(TestCase):
    def test_unicode(self):
        display = 'ClaimSubtype'
        data = mommy.make(ClaimSubtype, display=display)
        assert str(data) == display


class TestValueCodes(TestCase):
    def test_unicode(self):
        display = 'ValueCodes'
        data = mommy.make(ValueCodes, display=display)
        assert str(data) == display


class TestExDiagnosisrelatedgroup(TestCase):
    def test_unicode(self):
        display = 'ExDiagnosisrelatedgroup'
        data = mommy.make(ExDiagnosisrelatedgroup, display=display)
        assert str(data) == display


class TestExDiagnosistype(TestCase):
    def test_unicode(self):
        display = 'ExDiagnosistype'
        data = mommy.make(ExDiagnosistype, display=display)
        assert str(data) == display


class TestTeeth(TestCase):
    def test_unicode(self):
        display = 'Teeth'
        data = mommy.make(Teeth, display=display)
        assert str(data) == display


class TestExOnsettype(TestCase):
    def test_unicode(self):
        display = 'ExOnsettype'
        data = mommy.make(ExOnsettype, display=display)
        assert str(data) == display


class TestOralProsthodonticMaterial(TestCase):
    def test_unicode(self):
        display = 'OralProsthodonticMaterial'
        data = mommy.make(OralProsthodonticMaterial, display=display)
        assert str(data) == display


class TestExPaymenttype(TestCase):
    def test_unicode(self):
        display = 'ExPaymenttype'
        data = mommy.make(ExPaymenttype, display=display)
        assert str(data) == display


class TestServicePharmacy(TestCase):
    def test_unicode(self):
        display = 'ServicePharmacy'
        data = mommy.make(ServicePharmacy, display=display)
        assert str(data) == display


class TestExProgramCode(TestCase):
    def test_unicode(self):
        display = 'ExProgramCode'
        data = mommy.make(ExProgramCode, display=display)
        assert str(data) == display


class TestProviderQualification(TestCase):
    def test_unicode(self):
        display = 'ProviderQualification'
        data = mommy.make(ProviderQualification, display=display)
        assert str(data) == display


class TestRelatedClaimRelationship(TestCase):
    def test_unicode(self):
        display = 'RelatedClaimRelationship'
        data = mommy.make(RelatedClaimRelationship, display=display)
        assert str(data) == display


class TestServiceModifiers(TestCase):
    def test_unicode(self):
        display = 'ServiceModifiers'
        data = mommy.make(ServiceModifiers, display=display)
        assert str(data) == display


class TestServicePlace(TestCase):
    def test_unicode(self):
        display = 'ServicePlace'
        data = mommy.make(ServicePlace, display=display)
        assert str(data) == display


class TestServiceProduct(TestCase):
    def test_unicode(self):
        display = 'ServiceProduct'
        data = mommy.make(ServiceProduct, display=display)
        assert str(data) == display


class TestTooth(TestCase):
    def test_unicode(self):
        display = 'Tooth'
        data = mommy.make(Tooth, display=display)
        assert str(data) == display


class TestUdi(TestCase):
    def test_unicode(self):
        display = 'Udi'
        data = mommy.make(Udi, display=display)
        assert str(data) == display


class TestVisionProduct(TestCase):
    def test_unicode(self):
        display = 'VisionProduct'
        data = mommy.make(VisionProduct, display=display)
        assert str(data) == display


class TestExtensionContext(TestCase):
    def test_unicode(self):
        display = 'ExtensionContext'
        data = mommy.make(ExtensionContext, display=display)
        assert str(data) == display


class TestFilterOperator(TestCase):
    def test_unicode(self):
        display = 'FilterOperator'
        data = mommy.make(FilterOperator, display=display)
        assert str(data) == display


class TestFlagCategory(TestCase):
    def test_unicode(self):
        display = 'FlagCategory'
        data = mommy.make(FlagCategory, display=display)
        assert str(data) == display


class TestFlagPriority(TestCase):
    def test_unicode(self):
        display = 'FlagPriority'
        data = mommy.make(FlagPriority, display=display)
        assert str(data) == display


class TestFlagStatus(TestCase):
    def test_unicode(self):
        display = 'FlagStatus'
        data = mommy.make(FlagStatus, display=display)
        assert str(data) == display


class TestFmConditions(TestCase):
    def test_unicode(self):
        display = 'FmConditions'
        data = mommy.make(FmConditions, display=display)
        assert str(data) == display


class TestForms(TestCase):
    def test_unicode(self):
        display = 'Forms'
        data = mommy.make(Forms, display=display)
        assert str(data) == display


class TestFundsreserve(TestCase):
    def test_unicode(self):
        display = 'Fundsreserve'
        data = mommy.make(Fundsreserve, display=display)
        assert str(data) == display


class TestGoalAcceptanceStatus(TestCase):
    def test_unicode(self):
        display = 'GoalAcceptanceStatus'
        data = mommy.make(GoalAcceptanceStatus, display=display)
        assert str(data) == display


class TestGoalCategory(TestCase):
    def test_unicode(self):
        display = 'GoalCategory'
        data = mommy.make(GoalCategory, display=display)
        assert str(data) == display


class TestGoalPriority(TestCase):
    def test_unicode(self):
        display = 'GoalPriority'
        data = mommy.make(GoalPriority, display=display)
        assert str(data) == display


class TestGoalRelationshipType(TestCase):
    def test_unicode(self):
        display = 'GoalRelationshipType'
        data = mommy.make(GoalRelationshipType, display=display)
        assert str(data) == display


class TestGoalStatus(TestCase):
    def test_unicode(self):
        display = 'GoalStatus'
        data = mommy.make(GoalStatus, display=display)
        assert str(data) == display


class TestGoalStatusReason(TestCase):
    def test_unicode(self):
        display = 'GoalStatusReason'
        data = mommy.make(GoalStatusReason, display=display)
        assert str(data) == display


class TestGroupType(TestCase):
    def test_unicode(self):
        display = 'GroupType'
        data = mommy.make(GroupType, display=display)
        assert str(data) == display


class TestGroupingBehavior(TestCase):
    def test_unicode(self):
        display = 'GroupingBehavior'
        data = mommy.make(GroupingBehavior, display=display)
        assert str(data) == display


class TestGuidanceResponseStatus(TestCase):
    def test_unicode(self):
        display = 'GuidanceResponseStatus'
        data = mommy.make(GuidanceResponseStatus, display=display)
        assert str(data) == display


class TestGuideDependencyType(TestCase):
    def test_unicode(self):
        display = 'GuideDependencyType'
        data = mommy.make(GuideDependencyType, display=display)
        assert str(data) == display


class TestGuidePageKind(TestCase):
    def test_unicode(self):
        display = 'GuidePageKind'
        data = mommy.make(GuidePageKind, display=display)
        assert str(data) == display


class TestHistoryStatus(TestCase):
    def test_unicode(self):
        display = 'HistoryStatus'
        data = mommy.make(HistoryStatus, display=display)
        assert str(data) == display


class TestHttpVerb(TestCase):
    def test_unicode(self):
        display = 'HttpVerb'
        data = mommy.make(HttpVerb, display=display)
        assert str(data) == display


class TestIdentifierType(TestCase):
    def test_unicode(self):
        display = 'IdentifierType'
        data = mommy.make(IdentifierType, display=display)
        assert str(data) == display


class TestIdentifierUse(TestCase):
    def test_unicode(self):
        display = 'IdentifierUse'
        data = mommy.make(IdentifierUse, display=display)
        assert str(data) == display


class TestIdentityAssurancelevel(TestCase):
    def test_unicode(self):
        display = 'IdentityAssurancelevel'
        data = mommy.make(IdentityAssurancelevel, display=display)
        assert str(data) == display


class TestImmunizationRecommendationDateCriterion(TestCase):
    def test_unicode(self):
        display = 'ImmunizationRecommendationDateCriterion'
        data = mommy.make(
            ImmunizationRecommendationDateCriterion, display=display)
        assert str(data) == display


class TestImmunizationRecommendationStatus(TestCase):
    def test_unicode(self):
        display = 'ImmunizationRecommendationStatus'
        data = mommy.make(ImmunizationRecommendationStatus, display=display)
        assert str(data) == display


class TestIntervention(TestCase):
    def test_unicode(self):
        display = 'Intervention'
        data = mommy.make(Intervention, display=display)
        assert str(data) == display


class TestIssueSeverity(TestCase):
    def test_unicode(self):
        display = 'IssueSeverity'
        data = mommy.make(IssueSeverity, display=display)
        assert str(data) == display


class TestIssueType(TestCase):
    def test_unicode(self):
        display = 'IssueType'
        data = mommy.make(IssueType, display=display)
        assert str(data) == display


class TestItemType(TestCase):
    def test_unicode(self):
        display = 'ItemType'
        data = mommy.make(ItemType, display=display)
        assert str(data) == display


class TestLinkType(TestCase):
    def test_unicode(self):
        display = 'LinkType'
        data = mommy.make(LinkType, display=display)
        assert str(data) == display


class TestLinkageType(TestCase):
    def test_unicode(self):
        display = 'LinkageType'
        data = mommy.make(LinkageType, display=display)
        assert str(data) == display


class TestListEmptyReason(TestCase):
    def test_unicode(self):
        display = 'ListEmptyReason'
        data = mommy.make(ListEmptyReason, display=display)
        assert str(data) == display


class TestListExampleCodes(TestCase):
    def test_unicode(self):
        display = 'ListExampleCodes'
        data = mommy.make(ListExampleCodes, display=display)
        assert str(data) == display


class TestListMode(TestCase):
    def test_unicode(self):
        display = 'ListMode'
        data = mommy.make(ListMode, display=display)
        assert str(data) == display


class TestListOrder(TestCase):
    def test_unicode(self):
        display = 'ListOrder'
        data = mommy.make(ListOrder, display=display)
        assert str(data) == display


class TestListStatus(TestCase):
    def test_unicode(self):
        display = 'ListStatus'
        data = mommy.make(ListStatus, display=display)
        assert str(data) == display


class TestLocationMode(TestCase):
    def test_unicode(self):
        display = 'LocationMode'
        data = mommy.make(LocationMode, display=display)
        assert str(data) == display


class TestLocationPhysicalType(TestCase):
    def test_unicode(self):
        display = 'LocationPhysicalType'
        data = mommy.make(LocationPhysicalType, display=display)
        assert str(data) == display


class TestLocationStatus(TestCase):
    def test_unicode(self):
        display = 'LocationStatus'
        data = mommy.make(LocationStatus, display=display)
        assert str(data) == display


class TestMapContextType(TestCase):
    def test_unicode(self):
        display = 'MapContextType'
        data = mommy.make(MapContextType, display=display)
        assert str(data) == display


class TestMapInputMode(TestCase):
    def test_unicode(self):
        display = 'MapInputMode'
        data = mommy.make(MapInputMode, display=display)
        assert str(data) == display


class TestMapListMode(TestCase):
    def test_unicode(self):
        display = 'MapListMode'
        data = mommy.make(MapListMode, display=display)
        assert str(data) == display


class TestMapModelMode(TestCase):
    def test_unicode(self):
        display = 'MapModelMode'
        data = mommy.make(MapModelMode, display=display)
        assert str(data) == display


class TestMapTransform(TestCase):
    def test_unicode(self):
        display = 'MapTransform'
        data = mommy.make(MapTransform, display=display)
        assert str(data) == display


class TestMaritalStatus(TestCase):
    def test_unicode(self):
        display = 'MaritalStatus'
        data = mommy.make(MaritalStatus, display=display)
        assert str(data) == display


class TestMatchGrade(TestCase):
    def test_unicode(self):
        display = 'MatchGrade'
        data = mommy.make(MatchGrade, display=display)
        assert str(data) == display


class TestMeasureDataUsage(TestCase):
    def test_unicode(self):
        display = 'MeasureDataUsage'
        data = mommy.make(MeasureDataUsage, display=display)
        assert str(data) == display


class TestMeasurePopulation(TestCase):
    def test_unicode(self):
        display = 'MeasurePopulation'
        data = mommy.make(MeasurePopulation, display=display)
        assert str(data) == display


class TestMeasureReportStatus(TestCase):
    def test_unicode(self):
        display = 'MeasureReportStatus'
        data = mommy.make(MeasureReportStatus, display=display)
        assert str(data) == display


class TestMeasureReportType(TestCase):
    def test_unicode(self):
        display = 'MeasureReportType'
        data = mommy.make(MeasureReportType, display=display)
        assert str(data) == display


class TestMeasureScoring(TestCase):
    def test_unicode(self):
        display = 'MeasureScoring'
        data = mommy.make(MeasureScoring, display=display)
        assert str(data) == display


class TestMeasureType(TestCase):
    def test_unicode(self):
        display = 'MeasureType'
        data = mommy.make(MeasureType, display=display)
        assert str(data) == display


class TestMeasurementPrinciple(TestCase):
    def test_unicode(self):
        display = 'MeasurementPrinciple'
        data = mommy.make(MeasurementPrinciple, display=display)
        assert str(data) == display


class TestDigitalMediaSubtype(TestCase):
    def test_unicode(self):
        display = 'DigitalMediaSubtype'
        data = mommy.make(DigitalMediaSubtype, display=display)
        assert str(data) == display


class TestMedicationAdminStatus(TestCase):
    def test_unicode(self):
        display = 'MedicationAdminStatus'
        data = mommy.make(MedicationAdminStatus, display=display)
        assert str(data) == display


class TestMedicationDispenseStatus(TestCase):
    def test_unicode(self):
        display = 'MedicationDispenseStatus'
        data = mommy.make(MedicationDispenseStatus, display=display)
        assert str(data) == display


class TestMedicationOrderStatus(TestCase):
    def test_unicode(self):
        display = 'MedicationOrderStatus'
        data = mommy.make(MedicationOrderStatus, display=display)
        assert str(data) == display


class TestMedicationStatementStatus(TestCase):
    def test_unicode(self):
        display = 'MedicationStatementStatus'
        data = mommy.make(MedicationStatementStatus, display=display)
        assert str(data) == display


class TestMessageConformanceEventMode(TestCase):
    def test_unicode(self):
        display = 'MessageConformanceEventMode'
        data = mommy.make(MessageConformanceEventMode, display=display)
        assert str(data) == display


class TestMessageEvents(TestCase):
    def test_unicode(self):
        display = 'MessageEvents'
        data = mommy.make(MessageEvents, display=display)
        assert str(data) == display


class TestMessageReasonEncounter(TestCase):
    def test_unicode(self):
        display = 'MessageReasonEncounter'
        data = mommy.make(MessageReasonEncounter, display=display)
        assert str(data) == display


class TestMessageSignificanceCategory(TestCase):
    def test_unicode(self):
        display = 'MessageSignificanceCategory'
        data = mommy.make(MessageSignificanceCategory, display=display)
        assert str(data) == display


class TestMessageTransport(TestCase):
    def test_unicode(self):
        display = 'MessageTransport'
        data = mommy.make(MessageTransport, display=display)
        assert str(data) == display


class TestMetricCalibrationState(TestCase):
    def test_unicode(self):
        display = 'MetricCalibrationState'
        data = mommy.make(MetricCalibrationState, display=display)
        assert str(data) == display


class TestMetricCalibrationType(TestCase):
    def test_unicode(self):
        display = 'MetricCalibrationType'
        data = mommy.make(MetricCalibrationType, display=display)
        assert str(data) == display


class TestMetricCategory(TestCase):
    def test_unicode(self):
        display = 'MetricCategory'
        data = mommy.make(MetricCategory, display=display)
        assert str(data) == display


class TestMetricColor(TestCase):
    def test_unicode(self):
        display = 'MetricColor'
        data = mommy.make(MetricColor, display=display)
        assert str(data) == display


class TestMetricOperationalStatus(TestCase):
    def test_unicode(self):
        display = 'MetricOperationalStatus'
        data = mommy.make(MetricOperationalStatus, display=display)
        assert str(data) == display


class TestMissingToothReason(TestCase):
    def test_unicode(self):
        display = 'MissingToothReason'
        data = mommy.make(MissingToothReason, display=display)
        assert str(data) == display


class TestClaimModifiers(TestCase):
    def test_unicode(self):
        display = 'ClaimModifiers'
        data = mommy.make(ClaimModifiers, display=display)
        assert str(data) == display


class TestModuleMetadataContributor(TestCase):
    def test_unicode(self):
        display = 'ModuleMetadataContributor'
        data = mommy.make(ModuleMetadataContributor, display=display)
        assert str(data) == display


class TestModuleMetadataFocusType(TestCase):
    def test_unicode(self):
        display = 'ModuleMetadataFocusType'
        data = mommy.make(ModuleMetadataFocusType, display=display)
        assert str(data) == display


class TestModuleMetadataResourceType(TestCase):
    def test_unicode(self):
        display = 'ModuleMetadataResourceType'
        data = mommy.make(ModuleMetadataResourceType, display=display)
        assert str(data) == display


class TestModuleMetadataStatus(TestCase):
    def test_unicode(self):
        display = 'ModuleMetadataStatus'
        data = mommy.make(ModuleMetadataStatus, display=display)
        assert str(data) == display


class TestModuleMetadataType(TestCase):
    def test_unicode(self):
        display = 'ModuleMetadataType'
        data = mommy.make(ModuleMetadataType, display=display)
        assert str(data) == display


class TestNameUse(TestCase):
    def test_unicode(self):
        display = 'NameUse'
        data = mommy.make(NameUse, display=display)
        assert str(data) == display


class TestNamingsystemIdentifierType(TestCase):
    def test_unicode(self):
        display = 'NamingsystemIdentifierType'
        data = mommy.make(NamingsystemIdentifierType, display=display)
        assert str(data) == display


class TestNamingsystemType(TestCase):
    def test_unicode(self):
        display = 'NamingsystemType'
        data = mommy.make(NamingsystemType, display=display)
        assert str(data) == display


class TestNarrativeStatus(TestCase):
    def test_unicode(self):
        display = 'NarrativeStatus'
        data = mommy.make(NarrativeStatus, display=display)
        assert str(data) == display


class TestNetworkType(TestCase):
    def test_unicode(self):
        display = 'NetworkType'
        data = mommy.make(NetworkType, display=display)
        assert str(data) == display


class TestNoteType(TestCase):
    def test_unicode(self):
        display = 'NoteType'
        data = mommy.make(NoteType, display=display)
        assert str(data) == display


class TestNutritionOrderStatus(TestCase):
    def test_unicode(self):
        display = 'NutritionOrderStatus'
        data = mommy.make(NutritionOrderStatus, display=display)
        assert str(data) == display


class TestObjectLifecycle(TestCase):
    def test_unicode(self):
        display = 'ObjectLifecycle'
        data = mommy.make(ObjectLifecycle, display=display)
        assert str(data) == display


class TestObjectRole(TestCase):
    def test_unicode(self):
        display = 'ObjectRole'
        data = mommy.make(ObjectRole, display=display)
        assert str(data) == display


class TestObjectType(TestCase):
    def test_unicode(self):
        display = 'ObjectType'
        data = mommy.make(ObjectType, display=display)
        assert str(data) == display


class TestObservationCategory(TestCase):
    def test_unicode(self):
        display = 'ObservationCategory'
        data = mommy.make(ObservationCategory, display=display)
        assert str(data) == display


class TestObservationParamcode(TestCase):
    def test_unicode(self):
        display = 'ObservationParamcode'
        data = mommy.make(ObservationParamcode, display=display)
        assert str(data) == display


class TestObservationRelationshiptypes(TestCase):
    def test_unicode(self):
        display = 'ObservationRelationshiptypes'
        data = mommy.make(ObservationRelationshiptypes, display=display)
        assert str(data) == display


class TestObservationStatus(TestCase):
    def test_unicode(self):
        display = 'ObservationStatus'
        data = mommy.make(ObservationStatus, display=display)
        assert str(data) == display


class TestOperationKind(TestCase):
    def test_unicode(self):
        display = 'OperationKind'
        data = mommy.make(OperationKind, display=display)
        assert str(data) == display


class TestOperationOutcome(TestCase):
    def test_unicode(self):
        display = 'OperationOutcome'
        data = mommy.make(OperationOutcome, display=display)
        assert str(data) == display


class TestOperationParameterUse(TestCase):
    def test_unicode(self):
        display = 'OperationParameterUse'
        data = mommy.make(OperationParameterUse, display=display)
        assert str(data) == display


class TestOrderSetItemType(TestCase):
    def test_unicode(self):
        display = 'OrderSetItemType'
        data = mommy.make(OrderSetItemType, display=display)
        assert str(data) == display


class TestOrderSetParticipant(TestCase):
    def test_unicode(self):
        display = 'OrderSetParticipant'
        data = mommy.make(OrderSetParticipant, display=display)
        assert str(data) == display


class TestOrderStatus(TestCase):
    def test_unicode(self):
        display = 'OrderStatus'
        data = mommy.make(OrderStatus, display=display)
        assert str(data) == display


class TestOrganizationType(TestCase):
    def test_unicode(self):
        display = 'OrganizationType'
        data = mommy.make(OrganizationType, display=display)
        assert str(data) == display


class TestEncounterParticipantType(TestCase):
    def test_unicode(self):
        display = 'EncounterParticipantType'
        data = mommy.make(EncounterParticipantType, display=display)
        assert str(data) == display


class TestParticipantrequired(TestCase):
    def test_unicode(self):
        display = 'Participantrequired'
        data = mommy.make(Participantrequired, display=display)
        assert str(data) == display


class TestParticipationstatus(TestCase):
    def test_unicode(self):
        display = 'Participationstatus'
        data = mommy.make(Participationstatus, display=display)
        assert str(data) == display


class TestPatientContactRelationship(TestCase):
    def test_unicode(self):
        display = 'PatientContactRelationship'
        data = mommy.make(PatientContactRelationship, display=display)
        assert str(data) == display


class TestPatientMpiMatch(TestCase):
    def test_unicode(self):
        display = 'PatientMpiMatch'
        data = mommy.make(PatientMpiMatch, display=display)
        assert str(data) == display


class TestPayeetype(TestCase):
    def test_unicode(self):
        display = 'Payeetype'
        data = mommy.make(Payeetype, display=display)
        assert str(data) == display


class TestPaymentAdjustmentReason(TestCase):
    def test_unicode(self):
        display = 'PaymentAdjustmentReason'
        data = mommy.make(PaymentAdjustmentReason, display=display)
        assert str(data) == display


class TestPaymentType(TestCase):
    def test_unicode(self):
        display = 'PaymentType'
        data = mommy.make(PaymentType, display=display)
        assert str(data) == display


class TestPaymentStatus(TestCase):
    def test_unicode(self):
        display = 'PaymentStatus'
        data = mommy.make(PaymentStatus, display=display)
        assert str(data) == display


class TestPlanactionBehaviorType(TestCase):
    def test_unicode(self):
        display = 'PlanactionBehaviorType'
        data = mommy.make(PlanactionBehaviorType, display=display)
        assert str(data) == display


class TestPlanactionRelationshipAnchor(TestCase):
    def test_unicode(self):
        display = 'PlanactionRelationshipAnchor'
        data = mommy.make(PlanactionRelationshipAnchor, display=display)
        assert str(data) == display


class TestPlanactionRelationshipType(TestCase):
    def test_unicode(self):
        display = 'PlanactionRelationshipType'
        data = mommy.make(PlanactionRelationshipType, display=display)
        assert str(data) == display


class TestPlanactionType(TestCase):
    def test_unicode(self):
        display = 'PlanactionType'
        data = mommy.make(PlanactionType, display=display)
        assert str(data) == display


class TestPractitionerRole(TestCase):
    def test_unicode(self):
        display = 'PractitionerRole'
        data = mommy.make(PractitionerRole, display=display)
        assert str(data) == display


class TestPractitionerSpecialty(TestCase):
    def test_unicode(self):
        display = 'PractitionerSpecialty'
        data = mommy.make(PractitionerSpecialty, display=display)
        assert str(data) == display


class TestPrecheckBehavior(TestCase):
    def test_unicode(self):
        display = 'PrecheckBehavior'
        data = mommy.make(PrecheckBehavior, display=display)
        assert str(data) == display


class TestProcedureProgressStatusCodes(TestCase):
    def test_unicode(self):
        display = 'ProcedureProgressStatusCodes'
        data = mommy.make(ProcedureProgressStatusCodes, display=display)
        assert str(data) == display


class TestProcedureRelationshipType(TestCase):
    def test_unicode(self):
        display = 'ProcedureRelationshipType'
        data = mommy.make(ProcedureRelationshipType, display=display)
        assert str(data) == display


class TestProcedureRequestPriority(TestCase):
    def test_unicode(self):
        display = 'ProcedureRequestPriority'
        data = mommy.make(ProcedureRequestPriority, display=display)
        assert str(data) == display


class TestProcedureRequestStatus(TestCase):
    def test_unicode(self):
        display = 'ProcedureRequestStatus'
        data = mommy.make(ProcedureRequestStatus, display=display)
        assert str(data) == display


class TestProcedureStatus(TestCase):
    def test_unicode(self):
        display = 'ProcedureStatus'
        data = mommy.make(ProcedureStatus, display=display)
        assert str(data) == display


class TestProcessOutcome(TestCase):
    def test_unicode(self):
        display = 'ProcessOutcome'
        data = mommy.make(ProcessOutcome, display=display)
        assert str(data) == display


class TestProcessPriority(TestCase):
    def test_unicode(self):
        display = 'ProcessPriority'
        data = mommy.make(ProcessPriority, display=display)
        assert str(data) == display


class TestPropertyRepresentation(TestCase):
    def test_unicode(self):
        display = 'PropertyRepresentation'
        data = mommy.make(PropertyRepresentation, display=display)
        assert str(data) == display


class TestProtocolActivityCategory(TestCase):
    def test_unicode(self):
        display = 'ProtocolActivityCategory'
        data = mommy.make(ProtocolActivityCategory, display=display)
        assert str(data) == display


class TestProtocolStatus(TestCase):
    def test_unicode(self):
        display = 'ProtocolStatus'
        data = mommy.make(ProtocolStatus, display=display)
        assert str(data) == display


class TestProtocolType(TestCase):
    def test_unicode(self):
        display = 'ProtocolType'
        data = mommy.make(ProtocolType, display=display)
        assert str(data) == display


class TestProvenanceEntityRole(TestCase):
    def test_unicode(self):
        display = 'ProvenanceEntityRole'
        data = mommy.make(ProvenanceEntityRole, display=display)
        assert str(data) == display


class TestProvenanceAgentRole(TestCase):
    def test_unicode(self):
        display = 'ProvenanceAgentRole'
        data = mommy.make(ProvenanceAgentRole, display=display)
        assert str(data) == display


class TestProvenanceAgentType(TestCase):
    def test_unicode(self):
        display = 'ProvenanceAgentType'
        data = mommy.make(ProvenanceAgentType, display=display)
        assert str(data) == display


class TestQuantityComparator(TestCase):
    def test_unicode(self):
        display = 'QuantityComparator'
        data = mommy.make(QuantityComparator, display=display)
        assert str(data) == display


class TestQuestionMaxOccurs(TestCase):
    def test_unicode(self):
        display = 'QuestionMaxOccurs'
        data = mommy.make(QuestionMaxOccurs, display=display)
        assert str(data) == display


class TestQuestionnaireAnswersStatus(TestCase):
    def test_unicode(self):
        display = 'QuestionnaireAnswersStatus'
        data = mommy.make(QuestionnaireAnswersStatus, display=display)
        assert str(data) == display


class TestQuestionnaireDisplayCategory(TestCase):
    def test_unicode(self):
        display = 'QuestionnaireDisplayCategory'
        data = mommy.make(QuestionnaireDisplayCategory, display=display)
        assert str(data) == display


class TestQuestionnaireItemControl(TestCase):
    def test_unicode(self):
        display = 'QuestionnaireItemControl'
        data = mommy.make(QuestionnaireItemControl, display=display)
        assert str(data) == display


class TestQuestionnaireStatus(TestCase):
    def test_unicode(self):
        display = 'QuestionnaireStatus'
        data = mommy.make(QuestionnaireStatus, display=display)
        assert str(data) == display


class TestReactionEventCertainty(TestCase):
    def test_unicode(self):
        display = 'ReactionEventCertainty'
        data = mommy.make(ReactionEventCertainty, display=display)
        assert str(data) == display


class TestReactionEventSeverity(TestCase):
    def test_unicode(self):
        display = 'ReactionEventSeverity'
        data = mommy.make(ReactionEventSeverity, display=display)
        assert str(data) == display


class TestReasonMedicationGivenCodes(TestCase):
    def test_unicode(self):
        display = 'ReasonMedicationGivenCodes'
        data = mommy.make(ReasonMedicationGivenCodes, display=display)
        assert str(data) == display


class TestReasonMedicationNotGivenCodes(TestCase):
    def test_unicode(self):
        display = 'ReasonMedicationNotGivenCodes'
        data = mommy.make(ReasonMedicationNotGivenCodes, display=display)
        assert str(data) == display


class TestReferenceVersionRules(TestCase):
    def test_unicode(self):
        display = 'ReferenceVersionRules'
        data = mommy.make(ReferenceVersionRules, display=display)
        assert str(data) == display


class TestReferencerangeMeaning(TestCase):
    def test_unicode(self):
        display = 'ReferencerangeMeaning'
        data = mommy.make(ReferencerangeMeaning, display=display)
        assert str(data) == display


class TestReferralcategory(TestCase):
    def test_unicode(self):
        display = 'Referralcategory'
        data = mommy.make(Referralcategory, display=display)
        assert str(data) == display


class TestReferralstatus(TestCase):
    def test_unicode(self):
        display = 'Referralstatus'
        data = mommy.make(Referralstatus, display=display)
        assert str(data) == display


class TestRelationship(TestCase):
    def test_unicode(self):
        display = 'Relationship'
        data = mommy.make(Relationship, display=display)
        assert str(data) == display


class TestRemittanceOutcome(TestCase):
    def test_unicode(self):
        display = 'RemittanceOutcome'
        data = mommy.make(RemittanceOutcome, display=display)
        assert str(data) == display


class TestRequiredBehavior(TestCase):
    def test_unicode(self):
        display = 'RequiredBehavior'
        data = mommy.make(RequiredBehavior, display=display)
        assert str(data) == display


class TestResourceAggregationMode(TestCase):
    def test_unicode(self):
        display = 'ResourceAggregationMode'
        data = mommy.make(ResourceAggregationMode, display=display)
        assert str(data) == display


class TestResourceSlicingRules(TestCase):
    def test_unicode(self):
        display = 'ResourceSlicingRules'
        data = mommy.make(ResourceSlicingRules, display=display)
        assert str(data) == display


class TestResourceTypeLink(TestCase):
    def test_unicode(self):
        display = 'ResourceTypeLink'
        data = mommy.make(ResourceTypeLink, display=display)
        assert str(data) == display


class TestResourceTypes(TestCase):
    def test_unicode(self):
        display = 'ResourceTypes'
        data = mommy.make(ResourceTypes, display=display)
        assert str(data) == display


class TestResourceValidationMode(TestCase):
    def test_unicode(self):
        display = 'ResourceValidationMode'
        data = mommy.make(ResourceValidationMode, display=display)
        assert str(data) == display


class TestResponseCode(TestCase):
    def test_unicode(self):
        display = 'ResponseCode'
        data = mommy.make(ResponseCode, display=display)
        assert str(data) == display


class TestRestfulConformanceMode(TestCase):
    def test_unicode(self):
        display = 'RestfulConformanceMode'
        data = mommy.make(RestfulConformanceMode, display=display)
        assert str(data) == display


class TestRestfulInteraction(TestCase):
    def test_unicode(self):
        display = 'RestfulInteraction'
        data = mommy.make(RestfulInteraction, display=display)
        assert str(data) == display


class TestRestfulSecurityService(TestCase):
    def test_unicode(self):
        display = 'RestfulSecurityService'
        data = mommy.make(RestfulSecurityService, display=display)
        assert str(data) == display


class TestRiskProbability(TestCase):
    def test_unicode(self):
        display = 'RiskProbability'
        data = mommy.make(RiskProbability, display=display)
        assert str(data) == display


class TestRuleset(TestCase):
    def test_unicode(self):
        display = 'Ruleset'
        data = mommy.make(Ruleset, display=display)
        assert str(data) == display


class TestSearchEntryMode(TestCase):
    def test_unicode(self):
        display = 'SearchEntryMode'
        data = mommy.make(SearchEntryMode, display=display)
        assert str(data) == display


class TestSearchModifierCode(TestCase):
    def test_unicode(self):
        display = 'SearchModifierCode'
        data = mommy.make(SearchModifierCode, display=display)
        assert str(data) == display


class TestSearchParamType(TestCase):
    def test_unicode(self):
        display = 'SearchParamType'
        data = mommy.make(SearchParamType, display=display)
        assert str(data) == display


class TestSearchXpathUsage(TestCase):
    def test_unicode(self):
        display = 'SearchXpathUsage'
        data = mommy.make(SearchXpathUsage, display=display)
        assert str(data) == display


class TestAuditSourceType(TestCase):
    def test_unicode(self):
        display = 'AuditSourceType'
        data = mommy.make(AuditSourceType, display=display)
        assert str(data) == display


class TestSelectionBehavior(TestCase):
    def test_unicode(self):
        display = 'SelectionBehavior'
        data = mommy.make(SelectionBehavior, display=display)
        assert str(data) == display


class TestSequenceType(TestCase):
    def test_unicode(self):
        display = 'SequenceType'
        data = mommy.make(SequenceType, display=display)
        assert str(data) == display


class TestServiceCategory(TestCase):
    def test_unicode(self):
        display = 'ServiceCategory'
        data = mommy.make(ServiceCategory, display=display)
        assert str(data) == display


class TestServiceProvisionConditions(TestCase):
    def test_unicode(self):
        display = 'ServiceProvisionConditions'
        data = mommy.make(ServiceProvisionConditions, display=display)
        assert str(data) == display


class TestServiceReferralMethod(TestCase):
    def test_unicode(self):
        display = 'ServiceReferralMethod'
        data = mommy.make(ServiceReferralMethod, display=display)
        assert str(data) == display


class TestServiceType(TestCase):
    def test_unicode(self):
        display = 'ServiceType'
        data = mommy.make(ServiceType, display=display)
        assert str(data) == display


class TestIcd10Procedures(TestCase):
    def test_unicode(self):
        display = 'Icd10Procedures'
        data = mommy.make(Icd10Procedures, display=display)
        assert str(data) == display


class TestSlotstatus(TestCase):
    def test_unicode(self):
        display = 'Slotstatus'
        data = mommy.make(Slotstatus, display=display)
        assert str(data) == display


class TestSpecialValues(TestCase):
    def test_unicode(self):
        display = 'SpecialValues'
        data = mommy.make(SpecialValues, display=display)
        assert str(data) == display


class TestSpecimenStatus(TestCase):
    def test_unicode(self):
        display = 'SpecimenStatus'
        data = mommy.make(SpecimenStatus, display=display)
        assert str(data) == display


class TestStructureDefinitionKind(TestCase):
    def test_unicode(self):
        display = 'StructureDefinitionKind'
        data = mommy.make(StructureDefinitionKind, display=display)
        assert str(data) == display


class TestSubscriptionChannelType(TestCase):
    def test_unicode(self):
        display = 'SubscriptionChannelType'
        data = mommy.make(SubscriptionChannelType, display=display)
        assert str(data) == display


class TestSubscriptionStatus(TestCase):
    def test_unicode(self):
        display = 'SubscriptionStatus'
        data = mommy.make(SubscriptionStatus, display=display)
        assert str(data) == display


class TestSubscriptionTag(TestCase):
    def test_unicode(self):
        display = 'SubscriptionTag'
        data = mommy.make(SubscriptionTag, display=display)
        assert str(data) == display


class TestSubstanceCategory(TestCase):
    def test_unicode(self):
        display = 'SubstanceCategory'
        data = mommy.make(SubstanceCategory, display=display)
        assert str(data) == display


class TestSupplydeliveryType(TestCase):
    def test_unicode(self):
        display = 'SupplydeliveryType'
        data = mommy.make(SupplydeliveryType, display=display)
        assert str(data) == display


class TestSupplyrequestKind(TestCase):
    def test_unicode(self):
        display = 'SupplyrequestKind'
        data = mommy.make(SupplyrequestKind, display=display)
        assert str(data) == display


class TestSupplydeliveryStatus(TestCase):
    def test_unicode(self):
        display = 'SupplydeliveryStatus'
        data = mommy.make(SupplydeliveryStatus, display=display)
        assert str(data) == display


class TestSupplyrequestReason(TestCase):
    def test_unicode(self):
        display = 'SupplyrequestReason'
        data = mommy.make(SupplyrequestReason, display=display)
        assert str(data) == display


class TestSupplyrequestStatus(TestCase):
    def test_unicode(self):
        display = 'SupplyrequestStatus'
        data = mommy.make(SupplyrequestStatus, display=display)
        assert str(data) == display


class TestTaskPerformerType(TestCase):
    def test_unicode(self):
        display = 'TaskPerformerType'
        data = mommy.make(TaskPerformerType, display=display)
        assert str(data) == display


class TestTaskPriority(TestCase):
    def test_unicode(self):
        display = 'TaskPriority'
        data = mommy.make(TaskPriority, display=display)
        assert str(data) == display


class TestTaskStage(TestCase):
    def test_unicode(self):
        display = 'TaskStage'
        data = mommy.make(TaskStage, display=display)
        assert str(data) == display


class TestTaskStatus(TestCase):
    def test_unicode(self):
        display = 'TaskStatus'
        data = mommy.make(TaskStatus, display=display)
        assert str(data) == display


class TestTestscriptOperationCodes(TestCase):
    def test_unicode(self):
        display = 'TestscriptOperationCodes'
        data = mommy.make(TestscriptOperationCodes, display=display)
        assert str(data) == display


class TestTestscriptProfileDestinationTypes(TestCase):
    def test_unicode(self):
        display = 'TestscriptProfileDestinationTypes'
        data = mommy.make(TestscriptProfileDestinationTypes, display=display)
        assert str(data) == display


class TestTestscriptProfileOriginTypes(TestCase):
    def test_unicode(self):
        display = 'TestscriptProfileOriginTypes'
        data = mommy.make(TestscriptProfileOriginTypes, display=display)
        assert str(data) == display


class TestTransactionMode(TestCase):
    def test_unicode(self):
        display = 'TransactionMode'
        data = mommy.make(TransactionMode, display=display)
        assert str(data) == display


class TestTriggerType(TestCase):
    def test_unicode(self):
        display = 'TriggerType'
        data = mommy.make(TriggerType, display=display)
        assert str(data) == display


class TestTypeDerivationRule(TestCase):
    def test_unicode(self):
        display = 'TypeDerivationRule'
        data = mommy.make(TypeDerivationRule, display=display)
        assert str(data) == display


class TestUnknownContentCode(TestCase):
    def test_unicode(self):
        display = 'UnknownContentCode'
        data = mommy.make(UnknownContentCode, display=display)
        assert str(data) == display


class TestVaccinationProtocolDoseStatus(TestCase):
    def test_unicode(self):
        display = 'VaccinationProtocolDoseStatus'
        data = mommy.make(VaccinationProtocolDoseStatus, display=display)
        assert str(data) == display


class TestVaccinationProtocolDoseStatusReason(TestCase):
    def test_unicode(self):
        display = 'VaccinationProtocolDoseStatusReason'
        data = mommy.make(VaccinationProtocolDoseStatusReason, display=display)
        assert str(data) == display


class TestVariantState(TestCase):
    def test_unicode(self):
        display = 'VariantState'
        data = mommy.make(VariantState, display=display)
        assert str(data) == display


class TestVersioningPolicy(TestCase):
    def test_unicode(self):
        display = 'VersioningPolicy'
        data = mommy.make(VersioningPolicy, display=display)
        assert str(data) == display


class TestVisionBaseCodes(TestCase):
    def test_unicode(self):
        display = 'VisionBaseCodes'
        data = mommy.make(VisionBaseCodes, display=display)
        assert str(data) == display


class TestVisionEyeCodes(TestCase):
    def test_unicode(self):
        display = 'VisionEyeCodes'
        data = mommy.make(VisionEyeCodes, display=display)
        assert str(data) == display


class TestXdsRelationshipType(TestCase):
    def test_unicode(self):
        display = 'XdsRelationshipType'
        data = mommy.make(XdsRelationshipType, display=display)
        assert str(data) == display


class TestAcknowledgementcondition(TestCase):
    def test_unicode(self):
        display = 'Acknowledgementcondition'
        data = mommy.make(Acknowledgementcondition, display=display)
        assert str(data) == display


class TestAcknowledgementdetailcode(TestCase):
    def test_unicode(self):
        display = 'Acknowledgementdetailcode'
        data = mommy.make(Acknowledgementdetailcode, display=display)
        assert str(data) == display


class TestAcknowledgementdetailtype(TestCase):
    def test_unicode(self):
        display = 'Acknowledgementdetailtype'
        data = mommy.make(Acknowledgementdetailtype, display=display)
        assert str(data) == display


class TestAcknowledgementtype(TestCase):
    def test_unicode(self):
        display = 'Acknowledgementtype'
        data = mommy.make(Acknowledgementtype, display=display)
        assert str(data) == display


class TestActclass(TestCase):
    def test_unicode(self):
        display = 'Actclass'
        data = mommy.make(Actclass, display=display)
        assert str(data) == display


class TestActcode(TestCase):
    def test_unicode(self):
        display = 'Actcode'
        data = mommy.make(Actcode, display=display)
        assert str(data) == display


class TestActexposurelevelcode(TestCase):
    def test_unicode(self):
        display = 'Actexposurelevelcode'
        data = mommy.make(Actexposurelevelcode, display=display)
        assert str(data) == display


class TestActinvoiceelementmodifier(TestCase):
    def test_unicode(self):
        display = 'Actinvoiceelementmodifier'
        data = mommy.make(Actinvoiceelementmodifier, display=display)
        assert str(data) == display


class TestActmood(TestCase):
    def test_unicode(self):
        display = 'Actmood'
        data = mommy.make(Actmood, display=display)
        assert str(data) == display


class TestActpriority(TestCase):
    def test_unicode(self):
        display = 'Actpriority'
        data = mommy.make(Actpriority, display=display)
        assert str(data) == display


class TestActreason(TestCase):
    def test_unicode(self):
        display = 'Actreason'
        data = mommy.make(Actreason, display=display)
        assert str(data) == display


class TestActrelationshipcheckpoint(TestCase):
    def test_unicode(self):
        display = 'Actrelationshipcheckpoint'
        data = mommy.make(Actrelationshipcheckpoint, display=display)
        assert str(data) == display


class TestActrelationshipjoin(TestCase):
    def test_unicode(self):
        display = 'Actrelationshipjoin'
        data = mommy.make(Actrelationshipjoin, display=display)
        assert str(data) == display


class TestActrelationshipsplit(TestCase):
    def test_unicode(self):
        display = 'Actrelationshipsplit'
        data = mommy.make(Actrelationshipsplit, display=display)
        assert str(data) == display


class TestActrelationshipsubset(TestCase):
    def test_unicode(self):
        display = 'Actrelationshipsubset'
        data = mommy.make(Actrelationshipsubset, display=display)
        assert str(data) == display


class TestActrelationshiptype(TestCase):
    def test_unicode(self):
        display = 'Actrelationshiptype'
        data = mommy.make(Actrelationshiptype, display=display)
        assert str(data) == display


class TestActsite(TestCase):
    def test_unicode(self):
        display = 'Actsite'
        data = mommy.make(Actsite, display=display)
        assert str(data) == display


class TestActstatus(TestCase):
    def test_unicode(self):
        display = 'Actstatus'
        data = mommy.make(Actstatus, display=display)
        assert str(data) == display


class TestActusprivacylaw(TestCase):
    def test_unicode(self):
        display = 'Actusprivacylaw'
        data = mommy.make(Actusprivacylaw, display=display)
        assert str(data) == display


class TestActuncertainty(TestCase):
    def test_unicode(self):
        display = 'Actuncertainty'
        data = mommy.make(Actuncertainty, display=display)
        assert str(data) == display


class TestAddressparttype(TestCase):
    def test_unicode(self):
        display = 'Addressparttype'
        data = mommy.make(Addressparttype, display=display)
        assert str(data) == display


class TestAmericanindianalaskanativelanguages(TestCase):
    def test_unicode(self):
        display = 'Americanindianalaskanativelanguages'
        data = mommy.make(Americanindianalaskanativelanguages, display=display)
        assert str(data) == display


class TestCalendar(TestCase):
    def test_unicode(self):
        display = 'Calendar'
        data = mommy.make(Calendar, display=display)
        assert str(data) == display


class TestCalendarcycle(TestCase):
    def test_unicode(self):
        display = 'Calendarcycle'
        data = mommy.make(Calendarcycle, display=display)
        assert str(data) == display


class TestCalendartype(TestCase):
    def test_unicode(self):
        display = 'Calendartype'
        data = mommy.make(Calendartype, display=display)
        assert str(data) == display


class TestCharset(TestCase):
    def test_unicode(self):
        display = 'Charset'
        data = mommy.make(Charset, display=display)
        assert str(data) == display


class TestCodingrationale(TestCase):
    def test_unicode(self):
        display = 'Codingrationale'
        data = mommy.make(Codingrationale, display=display)
        assert str(data) == display


class TestCommunicationfunctiontype(TestCase):
    def test_unicode(self):
        display = 'Communicationfunctiontype'
        data = mommy.make(Communicationfunctiontype, display=display)
        assert str(data) == display


class TestCompressionalgorithm(TestCase):
    def test_unicode(self):
        display = 'Compressionalgorithm'
        data = mommy.make(Compressionalgorithm, display=display)
        assert str(data) == display


class TestConfidentiality(TestCase):
    def test_unicode(self):
        display = 'Confidentiality'
        data = mommy.make(Confidentiality, display=display)
        assert str(data) == display


class TestContainercap(TestCase):
    def test_unicode(self):
        display = 'Containercap'
        data = mommy.make(Containercap, display=display)
        assert str(data) == display


class TestContainerseparator(TestCase):
    def test_unicode(self):
        display = 'Containerseparator'
        data = mommy.make(Containerseparator, display=display)
        assert str(data) == display


class TestContentprocessingmode(TestCase):
    def test_unicode(self):
        display = 'Contentprocessingmode'
        data = mommy.make(Contentprocessingmode, display=display)
        assert str(data) == display


class TestContextcontrol(TestCase):
    def test_unicode(self):
        display = 'Contextcontrol'
        data = mommy.make(Contextcontrol, display=display)
        assert str(data) == display


class TestDataoperation(TestCase):
    def test_unicode(self):
        display = 'Dataoperation'
        data = mommy.make(Dataoperation, display=display)
        assert str(data) == display


class TestDevicealertlevel(TestCase):
    def test_unicode(self):
        display = 'Devicealertlevel'
        data = mommy.make(Devicealertlevel, display=display)
        assert str(data) == display


class TestDocumentcompletion(TestCase):
    def test_unicode(self):
        display = 'Documentcompletion'
        data = mommy.make(Documentcompletion, display=display)
        assert str(data) == display


class TestDocumentstorage(TestCase):
    def test_unicode(self):
        display = 'Documentstorage'
        data = mommy.make(Documentstorage, display=display)
        assert str(data) == display


class TestEducationlevel(TestCase):
    def test_unicode(self):
        display = 'Educationlevel'
        data = mommy.make(Educationlevel, display=display)
        assert str(data) == display


class TestEmployeejobclass(TestCase):
    def test_unicode(self):
        display = 'Employeejobclass'
        data = mommy.make(Employeejobclass, display=display)
        assert str(data) == display


class TestEncounteradmissionsource(TestCase):
    def test_unicode(self):
        display = 'Encounteradmissionsource'
        data = mommy.make(Encounteradmissionsource, display=display)
        assert str(data) == display


class TestEncounterspecialcourtesy(TestCase):
    def test_unicode(self):
        display = 'Encounterspecialcourtesy'
        data = mommy.make(Encounterspecialcourtesy, display=display)
        assert str(data) == display


class TestEntityclass(TestCase):
    def test_unicode(self):
        display = 'Entityclass'
        data = mommy.make(Entityclass, display=display)
        assert str(data) == display


class TestEntitycode(TestCase):
    def test_unicode(self):
        display = 'Entitycode'
        data = mommy.make(Entitycode, display=display)
        assert str(data) == display


class TestEntitydeterminer(TestCase):
    def test_unicode(self):
        display = 'Entitydeterminer'
        data = mommy.make(Entitydeterminer, display=display)
        assert str(data) == display


class TestEntityhandling(TestCase):
    def test_unicode(self):
        display = 'Entityhandling'
        data = mommy.make(Entityhandling, display=display)
        assert str(data) == display


class TestEntitynamepartqualifier(TestCase):
    def test_unicode(self):
        display = 'Entitynamepartqualifier'
        data = mommy.make(Entitynamepartqualifier, display=display)
        assert str(data) == display


class TestEntitynamepartqualifierr2(TestCase):
    def test_unicode(self):
        display = 'Entitynamepartqualifierr2'
        data = mommy.make(Entitynamepartqualifierr2, display=display)
        assert str(data) == display


class TestEntitynameparttype(TestCase):
    def test_unicode(self):
        display = 'Entitynameparttype'
        data = mommy.make(Entitynameparttype, display=display)
        assert str(data) == display


class TestEntitynameparttyper2(TestCase):
    def test_unicode(self):
        display = 'Entitynameparttyper2'
        data = mommy.make(Entitynameparttyper2, display=display)
        assert str(data) == display


class TestEntitynameuse(TestCase):
    def test_unicode(self):
        display = 'Entitynameuse'
        data = mommy.make(Entitynameuse, display=display)
        assert str(data) == display


class TestEntitynameuser2(TestCase):
    def test_unicode(self):
        display = 'Entitynameuser2'
        data = mommy.make(Entitynameuser2, display=display)
        assert str(data) == display


class TestEntityrisk(TestCase):
    def test_unicode(self):
        display = 'Entityrisk'
        data = mommy.make(Entityrisk, display=display)
        assert str(data) == display


class TestEntitystatus(TestCase):
    def test_unicode(self):
        display = 'Entitystatus'
        data = mommy.make(Entitystatus, display=display)
        assert str(data) == display


class TestEquipmentalertlevel(TestCase):
    def test_unicode(self):
        display = 'Equipmentalertlevel'
        data = mommy.make(Equipmentalertlevel, display=display)
        assert str(data) == display


class TestEthnicity(TestCase):
    def test_unicode(self):
        display = 'Ethnicity'
        data = mommy.make(Ethnicity, display=display)
        assert str(data) == display


class TestExposuremode(TestCase):
    def test_unicode(self):
        display = 'Exposuremode'
        data = mommy.make(Exposuremode, display=display)
        assert str(data) == display


class TestGtsabbreviation(TestCase):
    def test_unicode(self):
        display = 'Gtsabbreviation'
        data = mommy.make(Gtsabbreviation, display=display)
        assert str(data) == display


class TestGenderstatus(TestCase):
    def test_unicode(self):
        display = 'Genderstatus'
        data = mommy.make(Genderstatus, display=display)
        assert str(data) == display


class TestHl7updatemode(TestCase):
    def test_unicode(self):
        display = 'Hl7updatemode'
        data = mommy.make(Hl7updatemode, display=display)
        assert str(data) == display


class TestHtmllinktype(TestCase):
    def test_unicode(self):
        display = 'Htmllinktype'
        data = mommy.make(Htmllinktype, display=display)
        assert str(data) == display


class TestIdentifierreliability(TestCase):
    def test_unicode(self):
        display = 'Identifierreliability'
        data = mommy.make(Identifierreliability, display=display)
        assert str(data) == display


class TestIdentifierscope(TestCase):
    def test_unicode(self):
        display = 'Identifierscope'
        data = mommy.make(Identifierscope, display=display)
        assert str(data) == display


class TestIntegritycheckalgorithm(TestCase):
    def test_unicode(self):
        display = 'Integritycheckalgorithm'
        data = mommy.make(Integritycheckalgorithm, display=display)
        assert str(data) == display


class TestLanguageabilitymode(TestCase):
    def test_unicode(self):
        display = 'Languageabilitymode'
        data = mommy.make(Languageabilitymode, display=display)
        assert str(data) == display


class TestLanguageabilityproficiency(TestCase):
    def test_unicode(self):
        display = 'Languageabilityproficiency'
        data = mommy.make(Languageabilityproficiency, display=display)
        assert str(data) == display


class TestLivingarrangement(TestCase):
    def test_unicode(self):
        display = 'Livingarrangement'
        data = mommy.make(Livingarrangement, display=display)
        assert str(data) == display


class TestLocalmarkupignore(TestCase):
    def test_unicode(self):
        display = 'Localmarkupignore'
        data = mommy.make(Localmarkupignore, display=display)
        assert str(data) == display


class TestLocalremotecontrolstate(TestCase):
    def test_unicode(self):
        display = 'Localremotecontrolstate'
        data = mommy.make(Localremotecontrolstate, display=display)
        assert str(data) == display


class TestManagedparticipationstatus(TestCase):
    def test_unicode(self):
        display = 'Managedparticipationstatus'
        data = mommy.make(Managedparticipationstatus, display=display)
        assert str(data) == display


class TestMaprelationship(TestCase):
    def test_unicode(self):
        display = 'Maprelationship'
        data = mommy.make(Maprelationship, display=display)
        assert str(data) == display


class TestMessagewaitingpriority(TestCase):
    def test_unicode(self):
        display = 'Messagewaitingpriority'
        data = mommy.make(Messagewaitingpriority, display=display)
        assert str(data) == display


class TestModifyindicator(TestCase):
    def test_unicode(self):
        display = 'Modifyindicator'
        data = mommy.make(Modifyindicator, display=display)
        assert str(data) == display


class TestNullflavor(TestCase):
    def test_unicode(self):
        display = 'Nullflavor'
        data = mommy.make(Nullflavor, display=display)
        assert str(data) == display


class TestObservationinterpretation(TestCase):
    def test_unicode(self):
        display = 'Observationinterpretation'
        data = mommy.make(Observationinterpretation, display=display)
        assert str(data) == display


class TestObservationmethod(TestCase):
    def test_unicode(self):
        display = 'Observationmethod'
        data = mommy.make(Observationmethod, display=display)
        assert str(data) == display


class TestObservationvalue(TestCase):
    def test_unicode(self):
        display = 'Observationvalue'
        data = mommy.make(Observationvalue, display=display)
        assert str(data) == display


class TestParticipationfunction(TestCase):
    def test_unicode(self):
        display = 'Participationfunction'
        data = mommy.make(Participationfunction, display=display)
        assert str(data) == display


class TestParticipationmode(TestCase):
    def test_unicode(self):
        display = 'Participationmode'
        data = mommy.make(Participationmode, display=display)
        assert str(data) == display


class TestParticipationsignature(TestCase):
    def test_unicode(self):
        display = 'Participationsignature'
        data = mommy.make(Participationsignature, display=display)
        assert str(data) == display


class TestParticipationtype(TestCase):
    def test_unicode(self):
        display = 'Participationtype'
        data = mommy.make(Participationtype, display=display)
        assert str(data) == display


class TestPatientimportance(TestCase):
    def test_unicode(self):
        display = 'Patientimportance'
        data = mommy.make(Patientimportance, display=display)
        assert str(data) == display


class TestPaymentterms(TestCase):
    def test_unicode(self):
        display = 'Paymentterms'
        data = mommy.make(Paymentterms, display=display)
        assert str(data) == display


class TestPersondisabilitytype(TestCase):
    def test_unicode(self):
        display = 'Persondisabilitytype'
        data = mommy.make(Persondisabilitytype, display=display)
        assert str(data) == display


class TestProbabilitydistributiontype(TestCase):
    def test_unicode(self):
        display = 'Probabilitydistributiontype'
        data = mommy.make(Probabilitydistributiontype, display=display)
        assert str(data) == display


class TestProcessingid(TestCase):
    def test_unicode(self):
        display = 'Processingid'
        data = mommy.make(Processingid, display=display)
        assert str(data) == display


class TestProcessingmode(TestCase):
    def test_unicode(self):
        display = 'Processingmode'
        data = mommy.make(Processingmode, display=display)
        assert str(data) == display


class TestQueryparametervalue(TestCase):
    def test_unicode(self):
        display = 'Queryparametervalue'
        data = mommy.make(Queryparametervalue, display=display)
        assert str(data) == display


class TestQuerypriority(TestCase):
    def test_unicode(self):
        display = 'Querypriority'
        data = mommy.make(Querypriority, display=display)
        assert str(data) == display


class TestQueryrequestlimit(TestCase):
    def test_unicode(self):
        display = 'Queryrequestlimit'
        data = mommy.make(Queryrequestlimit, display=display)
        assert str(data) == display


class TestQueryresponse(TestCase):
    def test_unicode(self):
        display = 'Queryresponse'
        data = mommy.make(Queryresponse, display=display)
        assert str(data) == display


class TestQuerystatuscode(TestCase):
    def test_unicode(self):
        display = 'Querystatuscode'
        data = mommy.make(Querystatuscode, display=display)
        assert str(data) == display


class TestRace(TestCase):
    def test_unicode(self):
        display = 'Race'
        data = mommy.make(Race, display=display)
        assert str(data) == display


class TestRelationaloperator(TestCase):
    def test_unicode(self):
        display = 'Relationaloperator'
        data = mommy.make(Relationaloperator, display=display)
        assert str(data) == display


class TestRelationshipconjunction(TestCase):
    def test_unicode(self):
        display = 'Relationshipconjunction'
        data = mommy.make(Relationshipconjunction, display=display)
        assert str(data) == display


class TestReligiousaffiliation(TestCase):
    def test_unicode(self):
        display = 'Religiousaffiliation'
        data = mommy.make(Religiousaffiliation, display=display)
        assert str(data) == display


class TestResponselevel(TestCase):
    def test_unicode(self):
        display = 'Responselevel'
        data = mommy.make(Responselevel, display=display)
        assert str(data) == display


class TestResponsemodality(TestCase):
    def test_unicode(self):
        display = 'Responsemodality'
        data = mommy.make(Responsemodality, display=display)
        assert str(data) == display


class TestResponsemode(TestCase):
    def test_unicode(self):
        display = 'Responsemode'
        data = mommy.make(Responsemode, display=display)
        assert str(data) == display


class TestRoleclass(TestCase):
    def test_unicode(self):
        display = 'Roleclass'
        data = mommy.make(Roleclass, display=display)
        assert str(data) == display


class TestRolecode(TestCase):
    def test_unicode(self):
        display = 'Rolecode'
        data = mommy.make(Rolecode, display=display)
        assert str(data) == display


class TestRolelinkstatus(TestCase):
    def test_unicode(self):
        display = 'Rolelinkstatus'
        data = mommy.make(Rolelinkstatus, display=display)
        assert str(data) == display


class TestRolelinktype(TestCase):
    def test_unicode(self):
        display = 'Rolelinktype'
        data = mommy.make(Rolelinktype, display=display)
        assert str(data) == display


class TestRolestatus(TestCase):
    def test_unicode(self):
        display = 'Rolestatus'
        data = mommy.make(Rolestatus, display=display)
        assert str(data) == display


class TestRouteofadministration(TestCase):
    def test_unicode(self):
        display = 'Routeofadministration'
        data = mommy.make(Routeofadministration, display=display)
        assert str(data) == display


class TestSequencing(TestCase):
    def test_unicode(self):
        display = 'Sequencing'
        data = mommy.make(Sequencing, display=display)
        assert str(data) == display


class TestSetoperator(TestCase):
    def test_unicode(self):
        display = 'Setoperator'
        data = mommy.make(Setoperator, display=display)
        assert str(data) == display


class TestSpecimentype(TestCase):
    def test_unicode(self):
        display = 'Specimentype'
        data = mommy.make(Specimentype, display=display)
        assert str(data) == display


class TestSubstitutioncondition(TestCase):
    def test_unicode(self):
        display = 'Substitutioncondition'
        data = mommy.make(Substitutioncondition, display=display)
        assert str(data) == display


class TestTablecellhorizontalalign(TestCase):
    def test_unicode(self):
        display = 'Tablecellhorizontalalign'
        data = mommy.make(Tablecellhorizontalalign, display=display)
        assert str(data) == display


class TestTablecellscope(TestCase):
    def test_unicode(self):
        display = 'Tablecellscope'
        data = mommy.make(Tablecellscope, display=display)
        assert str(data) == display


class TestTablecellverticalalign(TestCase):
    def test_unicode(self):
        display = 'Tablecellverticalalign'
        data = mommy.make(Tablecellverticalalign, display=display)
        assert str(data) == display


class TestTableframe(TestCase):
    def test_unicode(self):
        display = 'Tableframe'
        data = mommy.make(Tableframe, display=display)
        assert str(data) == display


class TestTablerules(TestCase):
    def test_unicode(self):
        display = 'Tablerules'
        data = mommy.make(Tablerules, display=display)
        assert str(data) == display


class TestTargetawareness(TestCase):
    def test_unicode(self):
        display = 'Targetawareness'
        data = mommy.make(Targetawareness, display=display)
        assert str(data) == display


class TestTelecommunicationcapabilities(TestCase):
    def test_unicode(self):
        display = 'Telecommunicationcapabilities'
        data = mommy.make(Telecommunicationcapabilities, display=display)
        assert str(data) == display


class TestTimingevent(TestCase):
    def test_unicode(self):
        display = 'Timingevent'
        data = mommy.make(Timingevent, display=display)
        assert str(data) == display


class TestTransmissionrelationshiptypecode(TestCase):
    def test_unicode(self):
        display = 'Transmissionrelationshiptypecode'
        data = mommy.make(Transmissionrelationshiptypecode, display=display)
        assert str(data) == display


class TestTribalentityus(TestCase):
    def test_unicode(self):
        display = 'Tribalentityus'
        data = mommy.make(Tribalentityus, display=display)
        assert str(data) == display


class TestVaccinemanufacturer(TestCase):
    def test_unicode(self):
        display = 'Vaccinemanufacturer'
        data = mommy.make(Vaccinemanufacturer, display=display)
        assert str(data) == display


class TestHl7realm(TestCase):
    def test_unicode(self):
        display = 'Hl7realm'
        data = mommy.make(Hl7realm, display=display)
        assert str(data) == display


class TestHl7v3conformance(TestCase):
    def test_unicode(self):
        display = 'Hl7v3conformance'
        data = mommy.make(Hl7v3conformance, display=display)
        assert str(data) == display


class TestOrderabledrugform(TestCase):
    def test_unicode(self):
        display = 'Orderabledrugform'
        data = mommy.make(Orderabledrugform, display=display)
        assert str(data) == display


class TestSubstanceadminsubstitution(TestCase):
    def test_unicode(self):
        display = 'Substanceadminsubstitution'
        data = mommy.make(Substanceadminsubstitution, display=display)
        assert str(data) == display
