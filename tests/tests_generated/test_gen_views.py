from django.core.urlresolvers import reverse

from rest_framework.test import APITestCase

from fhir_valuesets.valuesets.models.generated_models import *  # noqa
from tests.test_valueset_views import BaseViewsTest


class TestExampleViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestExampleViewSet, self).setUp()
        self.url_list = reverse('valuesets:Example-list')
        self.url_detail = 'valuesets:Example-detail'
        self.model = Example
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestSurfaceViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestSurfaceViewSet, self).setUp()
        self.url_list = reverse('valuesets:Surface-list')
        self.url_detail = 'valuesets:Surface-detail'
        self.model = Surface
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestLoinc480020AnswerlistViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestLoinc480020AnswerlistViewSet, self).setUp()
        self.url_list = reverse(
            'valuesets:Loinc480020Answerlist-list')
        self.url_detail = 'valuesets:Loinc480020Answerlist-detail'
        self.model = Loinc480020Answerlist
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestLoinc480194AnswerlistViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestLoinc480194AnswerlistViewSet, self).setUp()
        self.url_list = reverse(
            'valuesets:Loinc480194Answerlist-list')
        self.url_detail = 'valuesets:Loinc480194Answerlist-detail'
        self.model = Loinc480194Answerlist
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestLoinc530345AnswerlistViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestLoinc530345AnswerlistViewSet, self).setUp()
        self.url_list = reverse('valuesets:Loinc530345Answerlist-list')
        self.url_detail = 'valuesets:Loinc530345Answerlist-detail'
        self.model = Loinc530345Answerlist
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestAbstractTypesViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestAbstractTypesViewSet, self).setUp()
        self.url_list = reverse('valuesets:AbstractTypes-list')
        self.url_detail = 'valuesets:AbstractTypes-detail'
        self.model = AbstractTypes
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestAccountStatusViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestAccountStatusViewSet, self).setUp()
        self.url_list = reverse('valuesets:AccountStatus-list')
        self.url_detail = 'valuesets:AccountStatus-detail'
        self.model = AccountStatus
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestActionBehaviorTypeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestActionBehaviorTypeViewSet, self).setUp()
        self.url_list = reverse('valuesets:ActionBehaviorType-list')
        self.url_detail = 'valuesets:ActionBehaviorType-detail'
        self.model = ActionBehaviorType
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestActionCardinalityBehaviorViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestActionCardinalityBehaviorViewSet, self).setUp()
        self.url_list = reverse('valuesets:ActionCardinalityBehavior-list')
        self.url_detail = 'valuesets:ActionCardinalityBehavior-detail'
        self.model = ActionCardinalityBehavior
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestActionGroupingBehaviorViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestActionGroupingBehaviorViewSet, self).setUp()
        self.url_list = reverse('valuesets:ActionGroupingBehavior-list')
        self.url_detail = 'valuesets:ActionGroupingBehavior-detail'
        self.model = ActionGroupingBehavior
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestActionParticipantTypeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestActionParticipantTypeViewSet, self).setUp()
        self.url_list = reverse('valuesets:ActionParticipantType-list')
        self.url_detail = 'valuesets:ActionParticipantType-detail'
        self.model = ActionParticipantType
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestActionPrecheckBehaviorViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestActionPrecheckBehaviorViewSet, self).setUp()
        self.url_list = reverse('valuesets:ActionPrecheckBehavior-list')
        self.url_detail = 'valuesets:ActionPrecheckBehavior-detail'
        self.model = ActionPrecheckBehavior
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestActionRelationshipAnchorViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestActionRelationshipAnchorViewSet, self).setUp()
        self.url_list = reverse('valuesets:ActionRelationshipAnchor-list')
        self.url_detail = 'valuesets:ActionRelationshipAnchor-detail'
        self.model = ActionRelationshipAnchor
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestActionRelationshipTypeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestActionRelationshipTypeViewSet, self).setUp()
        self.url_list = reverse('valuesets:ActionRelationshipType-list')
        self.url_detail = 'valuesets:ActionRelationshipType-detail'
        self.model = ActionRelationshipType
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestActionRequiredBehaviorViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestActionRequiredBehaviorViewSet, self).setUp()
        self.url_list = reverse('valuesets:ActionRequiredBehavior-list')
        self.url_detail = 'valuesets:ActionRequiredBehavior-detail'
        self.model = ActionRequiredBehavior
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestActionSelectionBehaviorViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestActionSelectionBehaviorViewSet, self).setUp()
        self.url_list = reverse('valuesets:ActionSelectionBehavior-list')
        self.url_detail = 'valuesets:ActionSelectionBehavior-detail'
        self.model = ActionSelectionBehavior
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestActionTypeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestActionTypeViewSet, self).setUp()
        self.url_list = reverse('valuesets:ActionType-list')
        self.url_detail = 'valuesets:ActionType-detail'
        self.model = ActionType
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestActionlistViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestActionlistViewSet, self).setUp()
        self.url_list = reverse('valuesets:Actionlist-list')
        self.url_detail = 'valuesets:Actionlist-detail'
        self.model = Actionlist
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestActivityDefinitionCategoryViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestActivityDefinitionCategoryViewSet, self).setUp()
        self.url_list = reverse('valuesets:ActivityDefinitionCategory-list')
        self.url_detail = 'valuesets:ActivityDefinitionCategory-detail'
        self.model = ActivityDefinitionCategory
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestActivityParticipantTypeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestActivityParticipantTypeViewSet, self).setUp()
        self.url_list = reverse('valuesets:ActivityParticipantType-list')
        self.url_detail = 'valuesets:ActivityParticipantType-detail'
        self.model = ActivityParticipantType
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestAdditionalmaterialsViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestAdditionalmaterialsViewSet, self).setUp()
        self.url_list = reverse('valuesets:Additionalmaterials-list')
        self.url_detail = 'valuesets:Additionalmaterials-detail'
        self.model = Additionalmaterials
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestAddressTypeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestAddressTypeViewSet, self).setUp()
        self.url_list = reverse('valuesets:AddressType-list')
        self.url_detail = 'valuesets:AddressType-detail'
        self.model = AddressType
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestAddressUseViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestAddressUseViewSet, self).setUp()
        self.url_list = reverse('valuesets:AddressUse-list')
        self.url_detail = 'valuesets:AddressUse-detail'
        self.model = AddressUse
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestAdjudicationViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestAdjudicationViewSet, self).setUp()
        self.url_list = reverse('valuesets:Adjudication-list')
        self.url_detail = 'valuesets:Adjudication-detail'
        self.model = Adjudication
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestAdjudicationErrorViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestAdjudicationErrorViewSet, self).setUp()
        self.url_list = reverse('valuesets:AdjudicationError-list')
        self.url_detail = 'valuesets:AdjudicationError-detail'
        self.model = AdjudicationError
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestAdjudicationReasonViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestAdjudicationReasonViewSet, self).setUp()
        self.url_list = reverse('valuesets:AdjudicationReason-list')
        self.url_detail = 'valuesets:AdjudicationReason-detail'
        self.model = AdjudicationReason
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestAdministrativeGenderViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestAdministrativeGenderViewSet, self).setUp()
        self.url_list = reverse('valuesets:AdministrativeGender-list')
        self.url_detail = 'valuesets:AdministrativeGender-detail'
        self.model = AdministrativeGender
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestEncounterAdmitSourceViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestEncounterAdmitSourceViewSet, self).setUp()
        self.url_list = reverse('valuesets:EncounterAdmitSource-list')
        self.url_detail = 'valuesets:EncounterAdmitSource-detail'
        self.model = EncounterAdmitSource
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestAllergyIntoleranceCategoryViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestAllergyIntoleranceCategoryViewSet, self).setUp()
        self.url_list = reverse('valuesets:AllergyIntoleranceCategory-list')
        self.url_detail = 'valuesets:AllergyIntoleranceCategory-detail'
        self.model = AllergyIntoleranceCategory
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestAllergyIntoleranceCriticalityViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestAllergyIntoleranceCriticalityViewSet, self).setUp()
        self.url_list = reverse(
            'valuesets:AllergyIntoleranceCriticality-list')
        self.url_detail = 'valuesets:AllergyIntoleranceCriticality-detail'
        self.model = AllergyIntoleranceCriticality
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestAllergyIntoleranceStatusViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestAllergyIntoleranceStatusViewSet, self).setUp()
        self.url_list = reverse('valuesets:AllergyIntoleranceStatus-list')
        self.url_detail = 'valuesets:AllergyIntoleranceStatus-detail'
        self.model = AllergyIntoleranceStatus
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestAllergyIntoleranceTypeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestAllergyIntoleranceTypeViewSet, self).setUp()
        self.url_list = reverse('valuesets:AllergyIntoleranceType-list')
        self.url_detail = 'valuesets:AllergyIntoleranceType-detail'
        self.model = AllergyIntoleranceType
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestAnimalBreedsViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestAnimalBreedsViewSet, self).setUp()
        self.url_list = reverse('valuesets:AnimalBreeds-list')
        self.url_detail = 'valuesets:AnimalBreeds-detail'
        self.model = AnimalBreeds
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestAnimalGenderstatusViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestAnimalGenderstatusViewSet, self).setUp()
        self.url_list = reverse('valuesets:AnimalGenderstatus-list')
        self.url_detail = 'valuesets:AnimalGenderstatus-detail'
        self.model = AnimalGenderstatus
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestAnimalSpeciesViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestAnimalSpeciesViewSet, self).setUp()
        self.url_list = reverse('valuesets:AnimalSpecies-list')
        self.url_detail = 'valuesets:AnimalSpecies-detail'
        self.model = AnimalSpecies
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestAppointmentstatusViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestAppointmentstatusViewSet, self).setUp()
        self.url_list = reverse('valuesets:Appointmentstatus-list')
        self.url_detail = 'valuesets:Appointmentstatus-detail'
        self.model = Appointmentstatus
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestAssertDirectionCodesViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestAssertDirectionCodesViewSet, self).setUp()
        self.url_list = reverse('valuesets:AssertDirectionCodes-list')
        self.url_detail = 'valuesets:AssertDirectionCodes-detail'
        self.model = AssertDirectionCodes
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestAssertOperatorCodesViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestAssertOperatorCodesViewSet, self).setUp()
        self.url_list = reverse('valuesets:AssertOperatorCodes-list')
        self.url_detail = 'valuesets:AssertOperatorCodes-detail'
        self.model = AssertOperatorCodes
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestAssertResponseCodeTypesViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestAssertResponseCodeTypesViewSet, self).setUp()
        self.url_list = reverse('valuesets:AssertResponseCodeTypes-list')
        self.url_detail = 'valuesets:AssertResponseCodeTypes-detail'
        self.model = AssertResponseCodeTypes
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestAuditEventActionViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestAuditEventActionViewSet, self).setUp()
        self.url_list = reverse('valuesets:AuditEventAction-list')
        self.url_detail = 'valuesets:AuditEventAction-detail'
        self.model = AuditEventAction
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestAuditEventOutcomeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestAuditEventOutcomeViewSet, self).setUp()
        self.url_list = reverse('valuesets:AuditEventOutcome-list')
        self.url_detail = 'valuesets:AuditEventOutcome-detail'
        self.model = AuditEventOutcome
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestAuditEventTypeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestAuditEventTypeViewSet, self).setUp()
        self.url_list = reverse('valuesets:AuditEventType-list')
        self.url_detail = 'valuesets:AuditEventType-detail'
        self.model = AuditEventType
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestBasicResourceTypeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestBasicResourceTypeViewSet, self).setUp()
        self.url_list = reverse('valuesets:BasicResourceType-list')
        self.url_detail = 'valuesets:BasicResourceType-detail'
        self.model = BasicResourceType
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestBenefitCategoryViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestBenefitCategoryViewSet, self).setUp()
        self.url_list = reverse('valuesets:BenefitCategory-list')
        self.url_detail = 'valuesets:BenefitCategory-detail'
        self.model = BenefitCategory
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestBenefitNetworkViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestBenefitNetworkViewSet, self).setUp()
        self.url_list = reverse('valuesets:BenefitNetwork-list')
        self.url_detail = 'valuesets:BenefitNetwork-detail'
        self.model = BenefitNetwork
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestBenefitSubcategoryViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestBenefitSubcategoryViewSet, self).setUp()
        self.url_list = reverse('valuesets:BenefitSubcategory-list')
        self.url_detail = 'valuesets:BenefitSubcategory-detail'
        self.model = BenefitSubcategory
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestBenefitTermViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestBenefitTermViewSet, self).setUp()
        self.url_list = reverse('valuesets:BenefitTerm-list')
        self.url_detail = 'valuesets:BenefitTerm-detail'
        self.model = BenefitTerm
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestBenefitTypeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestBenefitTypeViewSet, self).setUp()
        self.url_list = reverse('valuesets:BenefitType-list')
        self.url_detail = 'valuesets:BenefitType-detail'
        self.model = BenefitType
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestBenefitUnitViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestBenefitUnitViewSet, self).setUp()
        self.url_list = reverse('valuesets:BenefitUnit-list')
        self.url_detail = 'valuesets:BenefitUnit-detail'
        self.model = BenefitUnit
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestBindingStrengthViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestBindingStrengthViewSet, self).setUp()
        self.url_list = reverse('valuesets:BindingStrength-list')
        self.url_detail = 'valuesets:BindingStrength-detail'
        self.model = BindingStrength
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestBundleTypeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestBundleTypeViewSet, self).setUp()
        self.url_list = reverse('valuesets:BundleType-list')
        self.url_detail = 'valuesets:BundleType-detail'
        self.model = BundleType
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestCardinalityBehaviorViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestCardinalityBehaviorViewSet, self).setUp()
        self.url_list = reverse('valuesets:CardinalityBehavior-list')
        self.url_detail = 'valuesets:CardinalityBehavior-detail'
        self.model = CardinalityBehavior
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestCarePlanActivityCategoryViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestCarePlanActivityCategoryViewSet, self).setUp()
        self.url_list = reverse('valuesets:CarePlanActivityCategory-list')
        self.url_detail = 'valuesets:CarePlanActivityCategory-detail'
        self.model = CarePlanActivityCategory
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestCarePlanActivityStatusViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestCarePlanActivityStatusViewSet, self).setUp()
        self.url_list = reverse('valuesets:CarePlanActivityStatus-list')
        self.url_detail = 'valuesets:CarePlanActivityStatus-detail'
        self.model = CarePlanActivityStatus
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestCarePlanRelationshipViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestCarePlanRelationshipViewSet, self).setUp()
        self.url_list = reverse('valuesets:CarePlanRelationship-list')
        self.url_detail = 'valuesets:CarePlanRelationship-detail'
        self.model = CarePlanRelationship
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestCarePlanStatusViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestCarePlanStatusViewSet, self).setUp()
        self.url_list = reverse('valuesets:CarePlanStatus-list')
        self.url_detail = 'valuesets:CarePlanStatus-detail'
        self.model = CarePlanStatus
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestCdsRuleActionTypeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestCdsRuleActionTypeViewSet, self).setUp()
        self.url_list = reverse('valuesets:CdsRuleActionType-list')
        self.url_detail = 'valuesets:CdsRuleActionType-detail'
        self.model = CdsRuleActionType
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestCdsRuleParticipantViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestCdsRuleParticipantViewSet, self).setUp()
        self.url_list = reverse('valuesets:CdsRuleParticipant-list')
        self.url_detail = 'valuesets:CdsRuleParticipant-detail'
        self.model = CdsRuleParticipant
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestCdsRuleTriggerTypeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestCdsRuleTriggerTypeViewSet, self).setUp()
        self.url_list = reverse('valuesets:CdsRuleTriggerType-list')
        self.url_detail = 'valuesets:CdsRuleTriggerType-detail'
        self.model = CdsRuleTriggerType
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestChoiceListOrientationViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestChoiceListOrientationViewSet, self).setUp()
        self.url_list = reverse('valuesets:ChoiceListOrientation-list')
        self.url_detail = 'valuesets:ChoiceListOrientation-detail'
        self.model = ChoiceListOrientation
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestChromosomeHumanViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestChromosomeHumanViewSet, self).setUp()
        self.url_list = reverse('valuesets:ChromosomeHuman-list')
        self.url_detail = 'valuesets:ChromosomeHuman-detail'
        self.model = ChromosomeHuman
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestClaimExceptionViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestClaimExceptionViewSet, self).setUp()
        self.url_list = reverse('valuesets:ClaimException-list')
        self.url_detail = 'valuesets:ClaimException-detail'
        self.model = ClaimException
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestClaimTypeLinkViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestClaimTypeLinkViewSet, self).setUp()
        self.url_list = reverse('valuesets:ClaimTypeLink-list')
        self.url_detail = 'valuesets:ClaimTypeLink-detail'
        self.model = ClaimTypeLink
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestClaimTypeLink2ViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestClaimTypeLink2ViewSet, self).setUp()
        self.url_list = reverse('valuesets:ClaimTypeLink2-list')
        self.url_detail = 'valuesets:ClaimTypeLink2-detail'
        self.model = ClaimTypeLink2
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestClaimUseLinkViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestClaimUseLinkViewSet, self).setUp()
        self.url_list = reverse('valuesets:ClaimUseLink-list')
        self.url_detail = 'valuesets:ClaimUseLink-detail'
        self.model = ClaimUseLink
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestClaimCareteamroleViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestClaimCareteamroleViewSet, self).setUp()
        self.url_list = reverse('valuesets:ClaimCareteamrole-list')
        self.url_detail = 'valuesets:ClaimCareteamrole-detail'
        self.model = ClaimCareteamrole
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestClaimInformationcategoryViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestClaimInformationcategoryViewSet, self).setUp()
        self.url_list = reverse('valuesets:ClaimInformationcategory-list')
        self.url_detail = 'valuesets:ClaimInformationcategory-detail'
        self.model = ClaimInformationcategory
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestClassificationOrContextViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestClassificationOrContextViewSet, self).setUp()
        self.url_list = reverse('valuesets:ClassificationOrContext-list')
        self.url_detail = 'valuesets:ClassificationOrContext-detail'
        self.model = ClassificationOrContext
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestClinicalImpressionStatusViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestClinicalImpressionStatusViewSet, self).setUp()
        self.url_list = reverse('valuesets:ClinicalImpressionStatus-list')
        self.url_detail = 'valuesets:ClinicalImpressionStatus-detail'
        self.model = ClinicalImpressionStatus
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestContentModeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestContentModeViewSet, self).setUp()
        self.url_list = reverse('valuesets:ContentMode-list')
        self.url_detail = 'valuesets:ContentMode-detail'
        self.model = ContentMode
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestCommunicationRequestStatusViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestCommunicationRequestStatusViewSet, self).setUp()
        self.url_list = reverse('valuesets:CommunicationRequestStatus-list')
        self.url_detail = 'valuesets:CommunicationRequestStatus-detail'
        self.model = CommunicationRequestStatus
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestCommunicationStatusViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestCommunicationStatusViewSet, self).setUp()
        self.url_list = reverse('valuesets:CommunicationStatus-list')
        self.url_detail = 'valuesets:CommunicationStatus-detail'
        self.model = CommunicationStatus
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestCompartmentTypeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestCompartmentTypeViewSet, self).setUp()
        self.url_list = reverse('valuesets:CompartmentType-list')
        self.url_detail = 'valuesets:CompartmentType-detail'
        self.model = CompartmentType
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestCompositionAttestationModeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestCompositionAttestationModeViewSet, self).setUp()
        self.url_list = reverse('valuesets:CompositionAttestationMode-list')
        self.url_detail = 'valuesets:CompositionAttestationMode-detail'
        self.model = CompositionAttestationMode
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestCompositionStatusViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestCompositionStatusViewSet, self).setUp()
        self.url_list = reverse('valuesets:CompositionStatus-list')
        self.url_detail = 'valuesets:CompositionStatus-detail'
        self.model = CompositionStatus
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestConceptMapEquivalenceViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestConceptMapEquivalenceViewSet, self).setUp()
        self.url_list = reverse('valuesets:ConceptMapEquivalence-list')
        self.url_detail = 'valuesets:ConceptMapEquivalence-detail'
        self.model = ConceptMapEquivalence
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestConceptPropertiesViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestConceptPropertiesViewSet, self).setUp()
        self.url_list = reverse('valuesets:ConceptProperties-list')
        self.url_detail = 'valuesets:ConceptProperties-detail'
        self.model = ConceptProperties
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestConceptPropertyTypeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestConceptPropertyTypeViewSet, self).setUp()
        self.url_list = reverse('valuesets:ConceptPropertyType-list')
        self.url_detail = 'valuesets:ConceptPropertyType-detail'
        self.model = ConceptPropertyType
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestConditionCategoryViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestConditionCategoryViewSet, self).setUp()
        self.url_list = reverse('valuesets:ConditionCategory-list')
        self.url_detail = 'valuesets:ConditionCategory-detail'
        self.model = ConditionCategory
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestConditionClinicalViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestConditionClinicalViewSet, self).setUp()
        self.url_list = reverse('valuesets:ConditionClinical-list')
        self.url_detail = 'valuesets:ConditionClinical-detail'
        self.model = ConditionClinical
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestConditionStateViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestConditionStateViewSet, self).setUp()
        self.url_list = reverse('valuesets:ConditionState-list')
        self.url_detail = 'valuesets:ConditionState-detail'
        self.model = ConditionState
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestConditionVerStatusViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestConditionVerStatusViewSet, self).setUp()
        self.url_list = reverse('valuesets:ConditionVerStatus-list')
        self.url_detail = 'valuesets:ConditionVerStatus-detail'
        self.model = ConditionVerStatus
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestConditionalDeleteStatusViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestConditionalDeleteStatusViewSet, self).setUp()
        self.url_list = reverse('valuesets:ConditionalDeleteStatus-list')
        self.url_detail = 'valuesets:ConditionalDeleteStatus-detail'
        self.model = ConditionalDeleteStatus
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestConformanceExpectationViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestConformanceExpectationViewSet, self).setUp()
        self.url_list = reverse('valuesets:ConformanceExpectation-list')
        self.url_detail = 'valuesets:ConformanceExpectation-detail'
        self.model = ConformanceExpectation
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestConformanceResourceStatusViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestConformanceResourceStatusViewSet, self).setUp()
        self.url_list = reverse('valuesets:ConformanceResourceStatus-list')
        self.url_detail = 'valuesets:ConformanceResourceStatus-detail'
        self.model = ConformanceResourceStatus
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestConformanceStatementKindViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestConformanceStatementKindViewSet, self).setUp()
        self.url_list = reverse('valuesets:ConformanceStatementKind-list')
        self.url_detail = 'valuesets:ConformanceStatementKind-detail'
        self.model = ConformanceStatementKind
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestConsentDataMeaningViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestConsentDataMeaningViewSet, self).setUp()
        self.url_list = reverse('valuesets:ConsentDataMeaning-list')
        self.url_detail = 'valuesets:ConsentDataMeaning-detail'
        self.model = ConsentDataMeaning
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestConsentExceptTypeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestConsentExceptTypeViewSet, self).setUp()
        self.url_list = reverse('valuesets:ConsentExceptType-list')
        self.url_detail = 'valuesets:ConsentExceptType-detail'
        self.model = ConsentExceptType
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestConsentStatusViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestConsentStatusViewSet, self).setUp()
        self.url_list = reverse('valuesets:ConsentStatus-list')
        self.url_detail = 'valuesets:ConsentStatus-detail'
        self.model = ConsentStatus
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestConsentActionViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestConsentActionViewSet, self).setUp()
        self.url_list = reverse('valuesets:ConsentAction-list')
        self.url_detail = 'valuesets:ConsentAction-detail'
        self.model = ConsentAction
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestConsentCategoryViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestConsentCategoryViewSet, self).setUp()
        self.url_list = reverse('valuesets:ConsentCategory-list')
        self.url_detail = 'valuesets:ConsentCategory-detail'
        self.model = ConsentCategory
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestConstraintSeverityViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestConstraintSeverityViewSet, self).setUp()
        self.url_list = reverse('valuesets:ConstraintSeverity-list')
        self.url_detail = 'valuesets:ConstraintSeverity-detail'
        self.model = ConstraintSeverity
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestContactPointSystemViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestContactPointSystemViewSet, self).setUp()
        self.url_list = reverse('valuesets:ContactPointSystem-list')
        self.url_detail = 'valuesets:ContactPointSystem-detail'
        self.model = ContactPointSystem
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestContactPointUseViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestContactPointUseViewSet, self).setUp()
        self.url_list = reverse('valuesets:ContactPointUse-list')
        self.url_detail = 'valuesets:ContactPointUse-detail'
        self.model = ContactPointUse
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestContactentityTypeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestContactentityTypeViewSet, self).setUp()
        self.url_list = reverse('valuesets:ContactentityType-list')
        self.url_detail = 'valuesets:ContactentityType-detail'
        self.model = ContactentityType
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestContentTypeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestContentTypeViewSet, self).setUp()
        self.url_list = reverse('valuesets:ContentType-list')
        self.url_detail = 'valuesets:ContentType-detail'
        self.model = ContentType
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestContractSubtypeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestContractSubtypeViewSet, self).setUp()
        self.url_list = reverse('valuesets:ContractSubtype-list')
        self.url_detail = 'valuesets:ContractSubtype-detail'
        self.model = ContractSubtype
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestContractTermSubtypeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestContractTermSubtypeViewSet, self).setUp()
        self.url_list = reverse('valuesets:ContractTermSubtype-list')
        self.url_detail = 'valuesets:ContractTermSubtype-detail'
        self.model = ContractTermSubtype
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestContractTermTypeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestContractTermTypeViewSet, self).setUp()
        self.url_list = reverse('valuesets:ContractTermType-list')
        self.url_detail = 'valuesets:ContractTermType-detail'
        self.model = ContractTermType
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestContractTypeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestContractTypeViewSet, self).setUp()
        self.url_list = reverse('valuesets:ContractType-list')
        self.url_detail = 'valuesets:ContractType-detail'
        self.model = ContractType
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestCopyNumberEventViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestCopyNumberEventViewSet, self).setUp()
        self.url_list = reverse('valuesets:CopyNumberEvent-list')
        self.url_detail = 'valuesets:CopyNumberEvent-detail'
        self.model = CopyNumberEvent
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestCoverageExceptionViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestCoverageExceptionViewSet, self).setUp()
        self.url_list = reverse('valuesets:CoverageException-list')
        self.url_detail = 'valuesets:CoverageException-detail'
        self.model = CoverageException
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestDwebtypeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestDwebtypeViewSet, self).setUp()
        self.url_list = reverse('valuesets:Dwebtype-list')
        self.url_detail = 'valuesets:Dwebtype-detail'
        self.model = Dwebtype
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestDataAbsentReasonViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestDataAbsentReasonViewSet, self).setUp()
        self.url_list = reverse('valuesets:DataAbsentReason-list')
        self.url_detail = 'valuesets:DataAbsentReason-detail'
        self.model = DataAbsentReason
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestDataTypesViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestDataTypesViewSet, self).setUp()
        self.url_list = reverse('valuesets:DataTypes-list')
        self.url_detail = 'valuesets:DataTypes-detail'
        self.model = DataTypes
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestDataelementStringencyViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestDataelementStringencyViewSet, self).setUp()
        self.url_list = reverse('valuesets:DataelementStringency-list')
        self.url_detail = 'valuesets:DataelementStringency-detail'
        self.model = DataelementStringency
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestDaysOfWeekViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestDaysOfWeekViewSet, self).setUp()
        self.url_list = reverse('valuesets:DaysOfWeek-list')
        self.url_detail = 'valuesets:DaysOfWeek-detail'
        self.model = DaysOfWeek
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestDetectedissueSeverityViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestDetectedissueSeverityViewSet, self).setUp()
        self.url_list = reverse('valuesets:DetectedissueSeverity-list')
        self.url_detail = 'valuesets:DetectedissueSeverity-detail'
        self.model = DetectedissueSeverity
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestDeviceActionViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestDeviceActionViewSet, self).setUp()
        self.url_list = reverse('valuesets:DeviceAction-list')
        self.url_detail = 'valuesets:DeviceAction-detail'
        self.model = DeviceAction
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestDeviceUseRequestPriorityViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestDeviceUseRequestPriorityViewSet, self).setUp()
        self.url_list = reverse('valuesets:DeviceUseRequestPriority-list')
        self.url_detail = 'valuesets:DeviceUseRequestPriority-detail'
        self.model = DeviceUseRequestPriority
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestDeviceUseRequestStatusViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestDeviceUseRequestStatusViewSet, self).setUp()
        self.url_list = reverse('valuesets:DeviceUseRequestStatus-list')
        self.url_detail = 'valuesets:DeviceUseRequestStatus-detail'
        self.model = DeviceUseRequestStatus
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestDevicestatusViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestDevicestatusViewSet, self).setUp()
        self.url_list = reverse('valuesets:Devicestatus-list')
        self.url_detail = 'valuesets:Devicestatus-detail'
        self.model = Devicestatus
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestDiagnosticOrderPriorityViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestDiagnosticOrderPriorityViewSet, self).setUp()
        self.url_list = reverse('valuesets:DiagnosticOrderPriority-list')
        self.url_detail = 'valuesets:DiagnosticOrderPriority-detail'
        self.model = DiagnosticOrderPriority
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestDiagnosticOrderStatusViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestDiagnosticOrderStatusViewSet, self).setUp()
        self.url_list = reverse('valuesets:DiagnosticOrderStatus-list')
        self.url_detail = 'valuesets:DiagnosticOrderStatus-detail'
        self.model = DiagnosticOrderStatus
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestDiagnosticReportStatusViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestDiagnosticReportStatusViewSet, self).setUp()
        self.url_list = reverse('valuesets:DiagnosticReportStatus-list')
        self.url_detail = 'valuesets:DiagnosticReportStatus-detail'
        self.model = DiagnosticReportStatus
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestEncounterDietViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestEncounterDietViewSet, self).setUp()
        self.url_list = reverse('valuesets:EncounterDiet-list')
        self.url_detail = 'valuesets:EncounterDiet-detail'
        self.model = EncounterDiet
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestDigitalMediaTypeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestDigitalMediaTypeViewSet, self).setUp()
        self.url_list = reverse('valuesets:DigitalMediaType-list')
        self.url_detail = 'valuesets:DigitalMediaType-detail'
        self.model = DigitalMediaType
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestEncounterDischargeDispositionViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestEncounterDischargeDispositionViewSet, self).setUp()
        self.url_list = reverse(
            'valuesets:EncounterDischargeDisposition-list')
        self.url_detail = 'valuesets:EncounterDischargeDisposition-detail'
        self.model = EncounterDischargeDisposition
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestDocumentModeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestDocumentModeViewSet, self).setUp()
        self.url_list = reverse('valuesets:DocumentMode-list')
        self.url_detail = 'valuesets:DocumentMode-detail'
        self.model = DocumentMode
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestDocumentReferenceStatusViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestDocumentReferenceStatusViewSet, self).setUp()
        self.url_list = reverse(
            'valuesets:DocumentReferenceStatus-list')
        self.url_detail = 'valuesets:DocumentReferenceStatus-detail'
        self.model = DocumentReferenceStatus
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestDocumentRelationshipTypeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestDocumentRelationshipTypeViewSet, self).setUp()
        self.url_list = reverse(
            'valuesets:DocumentRelationshipType-list')
        self.url_detail = 'valuesets:DocumentRelationshipType-detail'
        self.model = DocumentRelationshipType
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestEncounterLocationStatusViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestEncounterLocationStatusViewSet, self).setUp()
        self.url_list = reverse('valuesets:EncounterLocationStatus-list')
        self.url_detail = 'valuesets:EncounterLocationStatus-detail'
        self.model = EncounterLocationStatus
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestEncounterPriorityViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestEncounterPriorityViewSet, self).setUp()
        self.url_list = reverse('valuesets:EncounterPriority-list')
        self.url_detail = 'valuesets:EncounterPriority-detail'
        self.model = EncounterPriority
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestEncounterSpecialArrangementsViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestEncounterSpecialArrangementsViewSet, self).setUp()
        self.url_list = reverse('valuesets:EncounterSpecialArrangements-list')
        self.url_detail = 'valuesets:EncounterSpecialArrangements-detail'
        self.model = EncounterSpecialArrangements
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestEncounterStateViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestEncounterStateViewSet, self).setUp()
        self.url_list = reverse('valuesets:EncounterState-list')
        self.url_detail = 'valuesets:EncounterState-detail'
        self.model = EncounterState
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestEncounterTypeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestEncounterTypeViewSet, self).setUp()
        self.url_list = reverse('valuesets:EncounterType-list')
        self.url_detail = 'valuesets:EncounterType-detail'
        self.model = EncounterType
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestEndpointStatusViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestEndpointStatusViewSet, self).setUp()
        self.url_list = reverse('valuesets:EndpointStatus-list')
        self.url_detail = 'valuesets:EndpointStatus-detail'
        self.model = EndpointStatus
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestEntformulaAdditiveViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestEntformulaAdditiveViewSet, self).setUp()
        self.url_list = reverse('valuesets:EntformulaAdditive-list')
        self.url_detail = 'valuesets:EntformulaAdditive-detail'
        self.model = EntformulaAdditive
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestEpisodeOfCareStatusViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestEpisodeOfCareStatusViewSet, self).setUp()
        self.url_list = reverse('valuesets:EpisodeOfCareStatus-list')
        self.url_detail = 'valuesets:EpisodeOfCareStatus-detail'
        self.model = EpisodeOfCareStatus
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestServiceUsclsViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestServiceUsclsViewSet, self).setUp()
        self.url_list = reverse('valuesets:ServiceUscls-list')
        self.url_detail = 'valuesets:ServiceUscls-detail'
        self.model = ServiceUscls
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestFmItemtypeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestFmItemtypeViewSet, self).setUp()
        self.url_list = reverse('valuesets:FmItemtype-list')
        self.url_detail = 'valuesets:FmItemtype-detail'
        self.model = FmItemtype
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestOccurrenceCodesViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestOccurrenceCodesViewSet, self).setUp()
        self.url_list = reverse('valuesets:OccurrenceCodes-list')
        self.url_detail = 'valuesets:OccurrenceCodes-detail'
        self.model = OccurrenceCodes
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestOccurrenceSpanCodesViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestOccurrenceSpanCodesViewSet, self).setUp()
        self.url_list = reverse('valuesets:OccurrenceSpanCodes-list')
        self.url_detail = 'valuesets:OccurrenceSpanCodes-detail'
        self.model = OccurrenceSpanCodes
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestClaimSubtypeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestClaimSubtypeViewSet, self).setUp()
        self.url_list = reverse('valuesets:ClaimSubtype-list')
        self.url_detail = 'valuesets:ClaimSubtype-detail'
        self.model = ClaimSubtype
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestValueCodesViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestValueCodesViewSet, self).setUp()
        self.url_list = reverse('valuesets:ValueCodes-list')
        self.url_detail = 'valuesets:ValueCodes-detail'
        self.model = ValueCodes
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestExDiagnosisrelatedgroupViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestExDiagnosisrelatedgroupViewSet, self).setUp()
        self.url_list = reverse('valuesets:ExDiagnosisrelatedgroup-list')
        self.url_detail = 'valuesets:ExDiagnosisrelatedgroup-detail'
        self.model = ExDiagnosisrelatedgroup
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestExDiagnosistypeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestExDiagnosistypeViewSet, self).setUp()
        self.url_list = reverse('valuesets:ExDiagnosistype-list')
        self.url_detail = 'valuesets:ExDiagnosistype-detail'
        self.model = ExDiagnosistype
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestTeethViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestTeethViewSet, self).setUp()
        self.url_list = reverse('valuesets:Teeth-list')
        self.url_detail = 'valuesets:Teeth-detail'
        self.model = Teeth
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestExOnsettypeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestExOnsettypeViewSet, self).setUp()
        self.url_list = reverse('valuesets:ExOnsettype-list')
        self.url_detail = 'valuesets:ExOnsettype-detail'
        self.model = ExOnsettype
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestOralProsthodonticMaterialViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestOralProsthodonticMaterialViewSet, self).setUp()
        self.url_list = reverse(
            'valuesets:OralProsthodonticMaterial-list')
        self.url_detail = 'valuesets:OralProsthodonticMaterial-detail'
        self.model = OralProsthodonticMaterial
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestExPaymenttypeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestExPaymenttypeViewSet, self).setUp()
        self.url_list = reverse('valuesets:ExPaymenttype-list')
        self.url_detail = 'valuesets:ExPaymenttype-detail'
        self.model = ExPaymenttype
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestServicePharmacyViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestServicePharmacyViewSet, self).setUp()
        self.url_list = reverse('valuesets:ServicePharmacy-list')
        self.url_detail = 'valuesets:ServicePharmacy-detail'
        self.model = ServicePharmacy
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestExProgramCodeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestExProgramCodeViewSet, self).setUp()
        self.url_list = reverse('valuesets:ExProgramCode-list')
        self.url_detail = 'valuesets:ExProgramCode-detail'
        self.model = ExProgramCode
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestProviderQualificationViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestProviderQualificationViewSet, self).setUp()
        self.url_list = reverse('valuesets:ProviderQualification-list')
        self.url_detail = 'valuesets:ProviderQualification-detail'
        self.model = ProviderQualification
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestRelatedClaimRelationshipViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestRelatedClaimRelationshipViewSet, self).setUp()
        self.url_list = reverse('valuesets:RelatedClaimRelationship-list')
        self.url_detail = 'valuesets:RelatedClaimRelationship-detail'
        self.model = RelatedClaimRelationship
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestServiceModifiersViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestServiceModifiersViewSet, self).setUp()
        self.url_list = reverse('valuesets:ServiceModifiers-list')
        self.url_detail = 'valuesets:ServiceModifiers-detail'
        self.model = ServiceModifiers
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestServicePlaceViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestServicePlaceViewSet, self).setUp()
        self.url_list = reverse('valuesets:ServicePlace-list')
        self.url_detail = 'valuesets:ServicePlace-detail'
        self.model = ServicePlace
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestServiceProductViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestServiceProductViewSet, self).setUp()
        self.url_list = reverse('valuesets:ServiceProduct-list')
        self.url_detail = 'valuesets:ServiceProduct-detail'
        self.model = ServiceProduct
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestToothViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestToothViewSet, self).setUp()
        self.url_list = reverse('valuesets:Tooth-list')
        self.url_detail = 'valuesets:Tooth-detail'
        self.model = Tooth
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestUdiViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestUdiViewSet, self).setUp()
        self.url_list = reverse('valuesets:Udi-list')
        self.url_detail = 'valuesets:Udi-detail'
        self.model = Udi
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestVisionProductViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestVisionProductViewSet, self).setUp()
        self.url_list = reverse('valuesets:VisionProduct-list')
        self.url_detail = 'valuesets:VisionProduct-detail'
        self.model = VisionProduct
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestExtensionContextViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestExtensionContextViewSet, self).setUp()
        self.url_list = reverse('valuesets:ExtensionContext-list')
        self.url_detail = 'valuesets:ExtensionContext-detail'
        self.model = ExtensionContext
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestFilterOperatorViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestFilterOperatorViewSet, self).setUp()
        self.url_list = reverse('valuesets:FilterOperator-list')
        self.url_detail = 'valuesets:FilterOperator-detail'
        self.model = FilterOperator
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestFlagCategoryViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestFlagCategoryViewSet, self).setUp()
        self.url_list = reverse('valuesets:FlagCategory-list')
        self.url_detail = 'valuesets:FlagCategory-detail'
        self.model = FlagCategory
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestFlagPriorityViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestFlagPriorityViewSet, self).setUp()
        self.url_list = reverse('valuesets:FlagPriority-list')
        self.url_detail = 'valuesets:FlagPriority-detail'
        self.model = FlagPriority
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestFlagStatusViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestFlagStatusViewSet, self).setUp()
        self.url_list = reverse('valuesets:FlagStatus-list')
        self.url_detail = 'valuesets:FlagStatus-detail'
        self.model = FlagStatus
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestFmConditionsViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestFmConditionsViewSet, self).setUp()
        self.url_list = reverse('valuesets:FmConditions-list')
        self.url_detail = 'valuesets:FmConditions-detail'
        self.model = FmConditions
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestFormsViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestFormsViewSet, self).setUp()
        self.url_list = reverse('valuesets:Forms-list')
        self.url_detail = 'valuesets:Forms-detail'
        self.model = Forms
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestFundsreserveViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestFundsreserveViewSet, self).setUp()
        self.url_list = reverse('valuesets:Fundsreserve-list')
        self.url_detail = 'valuesets:Fundsreserve-detail'
        self.model = Fundsreserve
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestGoalAcceptanceStatusViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestGoalAcceptanceStatusViewSet, self).setUp()
        self.url_list = reverse('valuesets:GoalAcceptanceStatus-list')
        self.url_detail = 'valuesets:GoalAcceptanceStatus-detail'
        self.model = GoalAcceptanceStatus
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestGoalCategoryViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestGoalCategoryViewSet, self).setUp()
        self.url_list = reverse('valuesets:GoalCategory-list')
        self.url_detail = 'valuesets:GoalCategory-detail'
        self.model = GoalCategory
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestGoalPriorityViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestGoalPriorityViewSet, self).setUp()
        self.url_list = reverse('valuesets:GoalPriority-list')
        self.url_detail = 'valuesets:GoalPriority-detail'
        self.model = GoalPriority
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestGoalRelationshipTypeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestGoalRelationshipTypeViewSet, self).setUp()
        self.url_list = reverse('valuesets:GoalRelationshipType-list')
        self.url_detail = 'valuesets:GoalRelationshipType-detail'
        self.model = GoalRelationshipType
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestGoalStatusViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestGoalStatusViewSet, self).setUp()
        self.url_list = reverse('valuesets:GoalStatus-list')
        self.url_detail = 'valuesets:GoalStatus-detail'
        self.model = GoalStatus
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestGoalStatusReasonViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestGoalStatusReasonViewSet, self).setUp()
        self.url_list = reverse('valuesets:GoalStatusReason-list')
        self.url_detail = 'valuesets:GoalStatusReason-detail'
        self.model = GoalStatusReason
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestGroupTypeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestGroupTypeViewSet, self).setUp()
        self.url_list = reverse('valuesets:GroupType-list')
        self.url_detail = 'valuesets:GroupType-detail'
        self.model = GroupType
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestGroupingBehaviorViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestGroupingBehaviorViewSet, self).setUp()
        self.url_list = reverse('valuesets:GroupingBehavior-list')
        self.url_detail = 'valuesets:GroupingBehavior-detail'
        self.model = GroupingBehavior
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestGuidanceResponseStatusViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestGuidanceResponseStatusViewSet, self).setUp()
        self.url_list = reverse('valuesets:GuidanceResponseStatus-list')
        self.url_detail = 'valuesets:GuidanceResponseStatus-detail'
        self.model = GuidanceResponseStatus
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestGuideDependencyTypeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestGuideDependencyTypeViewSet, self).setUp()
        self.url_list = reverse('valuesets:GuideDependencyType-list')
        self.url_detail = 'valuesets:GuideDependencyType-detail'
        self.model = GuideDependencyType
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestGuidePageKindViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestGuidePageKindViewSet, self).setUp()
        self.url_list = reverse('valuesets:GuidePageKind-list')
        self.url_detail = 'valuesets:GuidePageKind-detail'
        self.model = GuidePageKind
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestHistoryStatusViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestHistoryStatusViewSet, self).setUp()
        self.url_list = reverse('valuesets:HistoryStatus-list')
        self.url_detail = 'valuesets:HistoryStatus-detail'
        self.model = HistoryStatus
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestHttpVerbViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestHttpVerbViewSet, self).setUp()
        self.url_list = reverse('valuesets:HttpVerb-list')
        self.url_detail = 'valuesets:HttpVerb-detail'
        self.model = HttpVerb
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestIdentifierTypeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestIdentifierTypeViewSet, self).setUp()
        self.url_list = reverse('valuesets:IdentifierType-list')
        self.url_detail = 'valuesets:IdentifierType-detail'
        self.model = IdentifierType
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestIdentifierUseViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestIdentifierUseViewSet, self).setUp()
        self.url_list = reverse('valuesets:IdentifierUse-list')
        self.url_detail = 'valuesets:IdentifierUse-detail'
        self.model = IdentifierUse
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestIdentityAssurancelevelViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestIdentityAssurancelevelViewSet, self).setUp()
        self.url_list = reverse('valuesets:IdentityAssurancelevel-list')
        self.url_detail = 'valuesets:IdentityAssurancelevel-detail'
        self.model = IdentityAssurancelevel
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestImmunizationRecommendationDateCriterionViewSet(
        APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestImmunizationRecommendationDateCriterionViewSet, self).setUp()
        self.url_list = reverse(
            'valuesets:ImmunizationRecommendationDateCriterion-list')
        self.url_detail = (
            'valuesets:ImmunizationRecommendationDateCriterion-detail')
        self.model = ImmunizationRecommendationDateCriterion
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestImmunizationRecommendationStatusViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestImmunizationRecommendationStatusViewSet, self).setUp()
        self.url_list = reverse(
            'valuesets:ImmunizationRecommendationStatus-list')
        self.url_detail = 'valuesets:ImmunizationRecommendationStatus-detail'
        self.model = ImmunizationRecommendationStatus
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestInterventionViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestInterventionViewSet, self).setUp()
        self.url_list = reverse('valuesets:Intervention-list')
        self.url_detail = 'valuesets:Intervention-detail'
        self.model = Intervention
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestIssueSeverityViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestIssueSeverityViewSet, self).setUp()
        self.url_list = reverse('valuesets:IssueSeverity-list')
        self.url_detail = 'valuesets:IssueSeverity-detail'
        self.model = IssueSeverity
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestIssueTypeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestIssueTypeViewSet, self).setUp()
        self.url_list = reverse('valuesets:IssueType-list')
        self.url_detail = 'valuesets:IssueType-detail'
        self.model = IssueType
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestItemTypeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestItemTypeViewSet, self).setUp()
        self.url_list = reverse('valuesets:ItemType-list')
        self.url_detail = 'valuesets:ItemType-detail'
        self.model = ItemType
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestLinkTypeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestLinkTypeViewSet, self).setUp()
        self.url_list = reverse('valuesets:LinkType-list')
        self.url_detail = 'valuesets:LinkType-detail'
        self.model = LinkType
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestLinkageTypeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestLinkageTypeViewSet, self).setUp()
        self.url_list = reverse('valuesets:LinkageType-list')
        self.url_detail = 'valuesets:LinkageType-detail'
        self.model = LinkageType
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestListEmptyReasonViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestListEmptyReasonViewSet, self).setUp()
        self.url_list = reverse('valuesets:ListEmptyReason-list')
        self.url_detail = 'valuesets:ListEmptyReason-detail'
        self.model = ListEmptyReason
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestListExampleCodesViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestListExampleCodesViewSet, self).setUp()
        self.url_list = reverse('valuesets:ListExampleCodes-list')
        self.url_detail = 'valuesets:ListExampleCodes-detail'
        self.model = ListExampleCodes
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestListModeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestListModeViewSet, self).setUp()
        self.url_list = reverse('valuesets:ListMode-list')
        self.url_detail = 'valuesets:ListMode-detail'
        self.model = ListMode
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestListOrderViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestListOrderViewSet, self).setUp()
        self.url_list = reverse('valuesets:ListOrder-list')
        self.url_detail = 'valuesets:ListOrder-detail'
        self.model = ListOrder
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestListStatusViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestListStatusViewSet, self).setUp()
        self.url_list = reverse('valuesets:ListStatus-list')
        self.url_detail = 'valuesets:ListStatus-detail'
        self.model = ListStatus
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestLocationModeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestLocationModeViewSet, self).setUp()
        self.url_list = reverse('valuesets:LocationMode-list')
        self.url_detail = 'valuesets:LocationMode-detail'
        self.model = LocationMode
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestLocationPhysicalTypeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestLocationPhysicalTypeViewSet, self).setUp()
        self.url_list = reverse('valuesets:LocationPhysicalType-list')
        self.url_detail = 'valuesets:LocationPhysicalType-detail'
        self.model = LocationPhysicalType
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestLocationStatusViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestLocationStatusViewSet, self).setUp()
        self.url_list = reverse('valuesets:LocationStatus-list')
        self.url_detail = 'valuesets:LocationStatus-detail'
        self.model = LocationStatus
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestMapContextTypeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestMapContextTypeViewSet, self).setUp()
        self.url_list = reverse('valuesets:MapContextType-list')
        self.url_detail = 'valuesets:MapContextType-detail'
        self.model = MapContextType
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestMapInputModeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestMapInputModeViewSet, self).setUp()
        self.url_list = reverse('valuesets:MapInputMode-list')
        self.url_detail = 'valuesets:MapInputMode-detail'
        self.model = MapInputMode
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestMapListModeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestMapListModeViewSet, self).setUp()
        self.url_list = reverse('valuesets:MapListMode-list')
        self.url_detail = 'valuesets:MapListMode-detail'
        self.model = MapListMode
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestMapModelModeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestMapModelModeViewSet, self).setUp()
        self.url_list = reverse('valuesets:MapModelMode-list')
        self.url_detail = 'valuesets:MapModelMode-detail'
        self.model = MapModelMode
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestMapTransformViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestMapTransformViewSet, self).setUp()
        self.url_list = reverse('valuesets:MapTransform-list')
        self.url_detail = 'valuesets:MapTransform-detail'
        self.model = MapTransform
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestMaritalStatusViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestMaritalStatusViewSet, self).setUp()
        self.url_list = reverse('valuesets:MaritalStatus-list')
        self.url_detail = 'valuesets:MaritalStatus-detail'
        self.model = MaritalStatus
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestMatchGradeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestMatchGradeViewSet, self).setUp()
        self.url_list = reverse('valuesets:MatchGrade-list')
        self.url_detail = 'valuesets:MatchGrade-detail'
        self.model = MatchGrade
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestMeasureDataUsageViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestMeasureDataUsageViewSet, self).setUp()
        self.url_list = reverse('valuesets:MeasureDataUsage-list')
        self.url_detail = 'valuesets:MeasureDataUsage-detail'
        self.model = MeasureDataUsage
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestMeasurePopulationViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestMeasurePopulationViewSet, self).setUp()
        self.url_list = reverse('valuesets:MeasurePopulation-list')
        self.url_detail = 'valuesets:MeasurePopulation-detail'
        self.model = MeasurePopulation
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestMeasureReportStatusViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestMeasureReportStatusViewSet, self).setUp()
        self.url_list = reverse('valuesets:MeasureReportStatus-list')
        self.url_detail = 'valuesets:MeasureReportStatus-detail'
        self.model = MeasureReportStatus
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestMeasureReportTypeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestMeasureReportTypeViewSet, self).setUp()
        self.url_list = reverse('valuesets:MeasureReportType-list')
        self.url_detail = 'valuesets:MeasureReportType-detail'
        self.model = MeasureReportType
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestMeasureScoringViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestMeasureScoringViewSet, self).setUp()
        self.url_list = reverse('valuesets:MeasureScoring-list')
        self.url_detail = 'valuesets:MeasureScoring-detail'
        self.model = MeasureScoring
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestMeasureTypeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestMeasureTypeViewSet, self).setUp()
        self.url_list = reverse('valuesets:MeasureType-list')
        self.url_detail = 'valuesets:MeasureType-detail'
        self.model = MeasureType
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestMeasurementPrincipleViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestMeasurementPrincipleViewSet, self).setUp()
        self.url_list = reverse('valuesets:MeasurementPrinciple-list')
        self.url_detail = 'valuesets:MeasurementPrinciple-detail'
        self.model = MeasurementPrinciple
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestDigitalMediaSubtypeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestDigitalMediaSubtypeViewSet, self).setUp()
        self.url_list = reverse('valuesets:DigitalMediaSubtype-list')
        self.url_detail = 'valuesets:DigitalMediaSubtype-detail'
        self.model = DigitalMediaSubtype
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestMedicationAdminStatusViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestMedicationAdminStatusViewSet, self).setUp()
        self.url_list = reverse('valuesets:MedicationAdminStatus-list')
        self.url_detail = 'valuesets:MedicationAdminStatus-detail'
        self.model = MedicationAdminStatus
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestMedicationDispenseStatusViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestMedicationDispenseStatusViewSet, self).setUp()
        self.url_list = reverse('valuesets:MedicationDispenseStatus-list')
        self.url_detail = 'valuesets:MedicationDispenseStatus-detail'
        self.model = MedicationDispenseStatus
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestMedicationOrderStatusViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestMedicationOrderStatusViewSet, self).setUp()
        self.url_list = reverse('valuesets:MedicationOrderStatus-list')
        self.url_detail = 'valuesets:MedicationOrderStatus-detail'
        self.model = MedicationOrderStatus
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestMedicationStatementStatusViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestMedicationStatementStatusViewSet, self).setUp()
        self.url_list = reverse('valuesets:MedicationStatementStatus-list')
        self.url_detail = 'valuesets:MedicationStatementStatus-detail'
        self.model = MedicationStatementStatus
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestMessageConformanceEventModeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestMessageConformanceEventModeViewSet, self).setUp()
        self.url_list = reverse('valuesets:MessageConformanceEventMode-list')
        self.url_detail = 'valuesets:MessageConformanceEventMode-detail'
        self.model = MessageConformanceEventMode
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestMessageEventsViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestMessageEventsViewSet, self).setUp()
        self.url_list = reverse('valuesets:MessageEvents-list')
        self.url_detail = 'valuesets:MessageEvents-detail'
        self.model = MessageEvents
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestMessageReasonEncounterViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestMessageReasonEncounterViewSet, self).setUp()
        self.url_list = reverse('valuesets:MessageReasonEncounter-list')
        self.url_detail = 'valuesets:MessageReasonEncounter-detail'
        self.model = MessageReasonEncounter
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestMessageSignificanceCategoryViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestMessageSignificanceCategoryViewSet, self).setUp()
        self.url_list = reverse('valuesets:MessageSignificanceCategory-list')
        self.url_detail = 'valuesets:MessageSignificanceCategory-detail'
        self.model = MessageSignificanceCategory
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestMessageTransportViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestMessageTransportViewSet, self).setUp()
        self.url_list = reverse('valuesets:MessageTransport-list')
        self.url_detail = 'valuesets:MessageTransport-detail'
        self.model = MessageTransport
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestMetricCalibrationStateViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestMetricCalibrationStateViewSet, self).setUp()
        self.url_list = reverse('valuesets:MetricCalibrationState-list')
        self.url_detail = 'valuesets:MetricCalibrationState-detail'
        self.model = MetricCalibrationState
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestMetricCalibrationTypeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestMetricCalibrationTypeViewSet, self).setUp()
        self.url_list = reverse('valuesets:MetricCalibrationType-list')
        self.url_detail = 'valuesets:MetricCalibrationType-detail'
        self.model = MetricCalibrationType
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestMetricCategoryViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestMetricCategoryViewSet, self).setUp()
        self.url_list = reverse('valuesets:MetricCategory-list')
        self.url_detail = 'valuesets:MetricCategory-detail'
        self.model = MetricCategory
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestMetricColorViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestMetricColorViewSet, self).setUp()
        self.url_list = reverse('valuesets:MetricColor-list')
        self.url_detail = 'valuesets:MetricColor-detail'
        self.model = MetricColor
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestMetricOperationalStatusViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestMetricOperationalStatusViewSet, self).setUp()
        self.url_list = reverse('valuesets:MetricOperationalStatus-list')
        self.url_detail = 'valuesets:MetricOperationalStatus-detail'
        self.model = MetricOperationalStatus
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestMissingToothReasonViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestMissingToothReasonViewSet, self).setUp()
        self.url_list = reverse('valuesets:MissingToothReason-list')
        self.url_detail = 'valuesets:MissingToothReason-detail'
        self.model = MissingToothReason
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestClaimModifiersViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestClaimModifiersViewSet, self).setUp()
        self.url_list = reverse('valuesets:ClaimModifiers-list')
        self.url_detail = 'valuesets:ClaimModifiers-detail'
        self.model = ClaimModifiers
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestModuleMetadataContributorViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestModuleMetadataContributorViewSet, self).setUp()
        self.url_list = reverse('valuesets:ModuleMetadataContributor-list')
        self.url_detail = 'valuesets:ModuleMetadataContributor-detail'
        self.model = ModuleMetadataContributor
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestModuleMetadataFocusTypeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestModuleMetadataFocusTypeViewSet, self).setUp()
        self.url_list = reverse('valuesets:ModuleMetadataFocusType-list')
        self.url_detail = 'valuesets:ModuleMetadataFocusType-detail'
        self.model = ModuleMetadataFocusType
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestModuleMetadataResourceTypeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestModuleMetadataResourceTypeViewSet, self).setUp()
        self.url_list = reverse('valuesets:ModuleMetadataResourceType-list')
        self.url_detail = 'valuesets:ModuleMetadataResourceType-detail'
        self.model = ModuleMetadataResourceType
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestModuleMetadataStatusViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestModuleMetadataStatusViewSet, self).setUp()
        self.url_list = reverse('valuesets:ModuleMetadataStatus-list')
        self.url_detail = 'valuesets:ModuleMetadataStatus-detail'
        self.model = ModuleMetadataStatus
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestModuleMetadataTypeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestModuleMetadataTypeViewSet, self).setUp()
        self.url_list = reverse('valuesets:ModuleMetadataType-list')
        self.url_detail = 'valuesets:ModuleMetadataType-detail'
        self.model = ModuleMetadataType
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestNameUseViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestNameUseViewSet, self).setUp()
        self.url_list = reverse('valuesets:NameUse-list')
        self.url_detail = 'valuesets:NameUse-detail'
        self.model = NameUse
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestNamingsystemIdentifierTypeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestNamingsystemIdentifierTypeViewSet, self).setUp()
        self.url_list = reverse('valuesets:NamingsystemIdentifierType-list')
        self.url_detail = 'valuesets:NamingsystemIdentifierType-detail'
        self.model = NamingsystemIdentifierType
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestNamingsystemTypeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestNamingsystemTypeViewSet, self).setUp()
        self.url_list = reverse('valuesets:NamingsystemType-list')
        self.url_detail = 'valuesets:NamingsystemType-detail'
        self.model = NamingsystemType
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestNarrativeStatusViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestNarrativeStatusViewSet, self).setUp()
        self.url_list = reverse('valuesets:NarrativeStatus-list')
        self.url_detail = 'valuesets:NarrativeStatus-detail'
        self.model = NarrativeStatus
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestNetworkTypeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestNetworkTypeViewSet, self).setUp()
        self.url_list = reverse('valuesets:NetworkType-list')
        self.url_detail = 'valuesets:NetworkType-detail'
        self.model = NetworkType
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestNoteTypeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestNoteTypeViewSet, self).setUp()
        self.url_list = reverse('valuesets:NoteType-list')
        self.url_detail = 'valuesets:NoteType-detail'
        self.model = NoteType
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestNutritionOrderStatusViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestNutritionOrderStatusViewSet, self).setUp()
        self.url_list = reverse('valuesets:NutritionOrderStatus-list')
        self.url_detail = 'valuesets:NutritionOrderStatus-detail'
        self.model = NutritionOrderStatus
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestObjectLifecycleViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestObjectLifecycleViewSet, self).setUp()
        self.url_list = reverse('valuesets:ObjectLifecycle-list')
        self.url_detail = 'valuesets:ObjectLifecycle-detail'
        self.model = ObjectLifecycle
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestObjectRoleViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestObjectRoleViewSet, self).setUp()
        self.url_list = reverse('valuesets:ObjectRole-list')
        self.url_detail = 'valuesets:ObjectRole-detail'
        self.model = ObjectRole
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestObjectTypeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestObjectTypeViewSet, self).setUp()
        self.url_list = reverse('valuesets:ObjectType-list')
        self.url_detail = 'valuesets:ObjectType-detail'
        self.model = ObjectType
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestObservationCategoryViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestObservationCategoryViewSet, self).setUp()
        self.url_list = reverse('valuesets:ObservationCategory-list')
        self.url_detail = 'valuesets:ObservationCategory-detail'
        self.model = ObservationCategory
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestObservationParamcodeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestObservationParamcodeViewSet, self).setUp()
        self.url_list = reverse('valuesets:ObservationParamcode-list')
        self.url_detail = 'valuesets:ObservationParamcode-detail'
        self.model = ObservationParamcode
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestObservationRelationshiptypesViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestObservationRelationshiptypesViewSet, self).setUp()
        self.url_list = reverse('valuesets:ObservationRelationshiptypes-list')
        self.url_detail = 'valuesets:ObservationRelationshiptypes-detail'
        self.model = ObservationRelationshiptypes
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestObservationStatusViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestObservationStatusViewSet, self).setUp()
        self.url_list = reverse('valuesets:ObservationStatus-list')
        self.url_detail = 'valuesets:ObservationStatus-detail'
        self.model = ObservationStatus
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestOperationKindViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestOperationKindViewSet, self).setUp()
        self.url_list = reverse('valuesets:OperationKind-list')
        self.url_detail = 'valuesets:OperationKind-detail'
        self.model = OperationKind
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestOperationOutcomeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestOperationOutcomeViewSet, self).setUp()
        self.url_list = reverse('valuesets:OperationOutcome-list')
        self.url_detail = 'valuesets:OperationOutcome-detail'
        self.model = OperationOutcome
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestOperationParameterUseViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestOperationParameterUseViewSet, self).setUp()
        self.url_list = reverse('valuesets:OperationParameterUse-list')
        self.url_detail = 'valuesets:OperationParameterUse-detail'
        self.model = OperationParameterUse
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestOrderSetItemTypeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestOrderSetItemTypeViewSet, self).setUp()
        self.url_list = reverse('valuesets:OrderSetItemType-list')
        self.url_detail = 'valuesets:OrderSetItemType-detail'
        self.model = OrderSetItemType
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestOrderSetParticipantViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestOrderSetParticipantViewSet, self).setUp()
        self.url_list = reverse('valuesets:OrderSetParticipant-list')
        self.url_detail = 'valuesets:OrderSetParticipant-detail'
        self.model = OrderSetParticipant
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestOrderStatusViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestOrderStatusViewSet, self).setUp()
        self.url_list = reverse('valuesets:OrderStatus-list')
        self.url_detail = 'valuesets:OrderStatus-detail'
        self.model = OrderStatus
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestOrganizationTypeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestOrganizationTypeViewSet, self).setUp()
        self.url_list = reverse('valuesets:OrganizationType-list')
        self.url_detail = 'valuesets:OrganizationType-detail'
        self.model = OrganizationType
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestEncounterParticipantTypeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestEncounterParticipantTypeViewSet, self).setUp()
        self.url_list = reverse('valuesets:EncounterParticipantType-list')
        self.url_detail = 'valuesets:EncounterParticipantType-detail'
        self.model = EncounterParticipantType
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestParticipantrequiredViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestParticipantrequiredViewSet, self).setUp()
        self.url_list = reverse('valuesets:Participantrequired-list')
        self.url_detail = 'valuesets:Participantrequired-detail'
        self.model = Participantrequired
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestParticipationstatusViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestParticipationstatusViewSet, self).setUp()
        self.url_list = reverse('valuesets:Participationstatus-list')
        self.url_detail = 'valuesets:Participationstatus-detail'
        self.model = Participationstatus
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestPatientContactRelationshipViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestPatientContactRelationshipViewSet, self).setUp()
        self.url_list = reverse('valuesets:PatientContactRelationship-list')
        self.url_detail = 'valuesets:PatientContactRelationship-detail'
        self.model = PatientContactRelationship
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestPatientMpiMatchViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestPatientMpiMatchViewSet, self).setUp()
        self.url_list = reverse('valuesets:PatientMpiMatch-list')
        self.url_detail = 'valuesets:PatientMpiMatch-detail'
        self.model = PatientMpiMatch
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestPayeetypeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestPayeetypeViewSet, self).setUp()
        self.url_list = reverse('valuesets:Payeetype-list')
        self.url_detail = 'valuesets:Payeetype-detail'
        self.model = Payeetype
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestPaymentAdjustmentReasonViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestPaymentAdjustmentReasonViewSet, self).setUp()
        self.url_list = reverse('valuesets:PaymentAdjustmentReason-list')
        self.url_detail = 'valuesets:PaymentAdjustmentReason-detail'
        self.model = PaymentAdjustmentReason
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestPaymentTypeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestPaymentTypeViewSet, self).setUp()
        self.url_list = reverse('valuesets:PaymentType-list')
        self.url_detail = 'valuesets:PaymentType-detail'
        self.model = PaymentType
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestPaymentStatusViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestPaymentStatusViewSet, self).setUp()
        self.url_list = reverse('valuesets:PaymentStatus-list')
        self.url_detail = 'valuesets:PaymentStatus-detail'
        self.model = PaymentStatus
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestPlanactionBehaviorTypeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestPlanactionBehaviorTypeViewSet, self).setUp()
        self.url_list = reverse('valuesets:PlanactionBehaviorType-list')
        self.url_detail = 'valuesets:PlanactionBehaviorType-detail'
        self.model = PlanactionBehaviorType
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestPlanactionRelationshipAnchorViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestPlanactionRelationshipAnchorViewSet, self).setUp()
        self.url_list = reverse('valuesets:PlanactionRelationshipAnchor-list')
        self.url_detail = 'valuesets:PlanactionRelationshipAnchor-detail'
        self.model = PlanactionRelationshipAnchor
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestPlanactionRelationshipTypeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestPlanactionRelationshipTypeViewSet, self).setUp()
        self.url_list = reverse('valuesets:PlanactionRelationshipType-list')
        self.url_detail = 'valuesets:PlanactionRelationshipType-detail'
        self.model = PlanactionRelationshipType
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestPlanactionTypeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestPlanactionTypeViewSet, self).setUp()
        self.url_list = reverse('valuesets:PlanactionType-list')
        self.url_detail = 'valuesets:PlanactionType-detail'
        self.model = PlanactionType
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestPractitionerRoleViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestPractitionerRoleViewSet, self).setUp()
        self.url_list = reverse('valuesets:PractitionerRole-list')
        self.url_detail = 'valuesets:PractitionerRole-detail'
        self.model = PractitionerRole
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestPractitionerSpecialtyViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestPractitionerSpecialtyViewSet, self).setUp()
        self.url_list = reverse('valuesets:PractitionerSpecialty-list')
        self.url_detail = 'valuesets:PractitionerSpecialty-detail'
        self.model = PractitionerSpecialty
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestPrecheckBehaviorViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestPrecheckBehaviorViewSet, self).setUp()
        self.url_list = reverse('valuesets:PrecheckBehavior-list')
        self.url_detail = 'valuesets:PrecheckBehavior-detail'
        self.model = PrecheckBehavior
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestProcedureProgressStatusCodesViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestProcedureProgressStatusCodesViewSet, self).setUp()
        self.url_list = reverse(
            'valuesets:ProcedureProgressStatusCodes-list')
        self.url_detail = 'valuesets:ProcedureProgressStatusCodes-detail'
        self.model = ProcedureProgressStatusCodes
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestProcedureRelationshipTypeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestProcedureRelationshipTypeViewSet, self).setUp()
        self.url_list = reverse('valuesets:ProcedureRelationshipType-list')
        self.url_detail = 'valuesets:ProcedureRelationshipType-detail'
        self.model = ProcedureRelationshipType
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestProcedureRequestPriorityViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestProcedureRequestPriorityViewSet, self).setUp()
        self.url_list = reverse('valuesets:ProcedureRequestPriority-list')
        self.url_detail = 'valuesets:ProcedureRequestPriority-detail'
        self.model = ProcedureRequestPriority
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestProcedureRequestStatusViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestProcedureRequestStatusViewSet, self).setUp()
        self.url_list = reverse('valuesets:ProcedureRequestStatus-list')
        self.url_detail = 'valuesets:ProcedureRequestStatus-detail'
        self.model = ProcedureRequestStatus
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestProcedureStatusViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestProcedureStatusViewSet, self).setUp()
        self.url_list = reverse('valuesets:ProcedureStatus-list')
        self.url_detail = 'valuesets:ProcedureStatus-detail'
        self.model = ProcedureStatus
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestProcessOutcomeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestProcessOutcomeViewSet, self).setUp()
        self.url_list = reverse('valuesets:ProcessOutcome-list')
        self.url_detail = 'valuesets:ProcessOutcome-detail'
        self.model = ProcessOutcome
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestProcessPriorityViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestProcessPriorityViewSet, self).setUp()
        self.url_list = reverse('valuesets:ProcessPriority-list')
        self.url_detail = 'valuesets:ProcessPriority-detail'
        self.model = ProcessPriority
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestPropertyRepresentationViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestPropertyRepresentationViewSet, self).setUp()
        self.url_list = reverse('valuesets:PropertyRepresentation-list')
        self.url_detail = 'valuesets:PropertyRepresentation-detail'
        self.model = PropertyRepresentation
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestProtocolActivityCategoryViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestProtocolActivityCategoryViewSet, self).setUp()
        self.url_list = reverse('valuesets:ProtocolActivityCategory-list')
        self.url_detail = 'valuesets:ProtocolActivityCategory-detail'
        self.model = ProtocolActivityCategory
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestProtocolStatusViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestProtocolStatusViewSet, self).setUp()
        self.url_list = reverse('valuesets:ProtocolStatus-list')
        self.url_detail = 'valuesets:ProtocolStatus-detail'
        self.model = ProtocolStatus
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestProtocolTypeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestProtocolTypeViewSet, self).setUp()
        self.url_list = reverse('valuesets:ProtocolType-list')
        self.url_detail = 'valuesets:ProtocolType-detail'
        self.model = ProtocolType
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestProvenanceEntityRoleViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestProvenanceEntityRoleViewSet, self).setUp()
        self.url_list = reverse('valuesets:ProvenanceEntityRole-list')
        self.url_detail = 'valuesets:ProvenanceEntityRole-detail'
        self.model = ProvenanceEntityRole
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestProvenanceAgentRoleViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestProvenanceAgentRoleViewSet, self).setUp()
        self.url_list = reverse('valuesets:ProvenanceAgentRole-list')
        self.url_detail = 'valuesets:ProvenanceAgentRole-detail'
        self.model = ProvenanceAgentRole
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestProvenanceAgentTypeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestProvenanceAgentTypeViewSet, self).setUp()
        self.url_list = reverse('valuesets:ProvenanceAgentType-list')
        self.url_detail = 'valuesets:ProvenanceAgentType-detail'
        self.model = ProvenanceAgentType
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestQuantityComparatorViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestQuantityComparatorViewSet, self).setUp()
        self.url_list = reverse('valuesets:QuantityComparator-list')
        self.url_detail = 'valuesets:QuantityComparator-detail'
        self.model = QuantityComparator
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestQuestionMaxOccursViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestQuestionMaxOccursViewSet, self).setUp()
        self.url_list = reverse('valuesets:QuestionMaxOccurs-list')
        self.url_detail = 'valuesets:QuestionMaxOccurs-detail'
        self.model = QuestionMaxOccurs
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestQuestionnaireAnswersStatusViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestQuestionnaireAnswersStatusViewSet, self).setUp()
        self.url_list = reverse('valuesets:QuestionnaireAnswersStatus-list')
        self.url_detail = 'valuesets:QuestionnaireAnswersStatus-detail'
        self.model = QuestionnaireAnswersStatus
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestQuestionnaireDisplayCategoryViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestQuestionnaireDisplayCategoryViewSet, self).setUp()
        self.url_list = reverse('valuesets:QuestionnaireDisplayCategory-list')
        self.url_detail = 'valuesets:QuestionnaireDisplayCategory-detail'
        self.model = QuestionnaireDisplayCategory
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestQuestionnaireItemControlViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestQuestionnaireItemControlViewSet, self).setUp()
        self.url_list = reverse('valuesets:QuestionnaireItemControl-list')
        self.url_detail = 'valuesets:QuestionnaireItemControl-detail'
        self.model = QuestionnaireItemControl
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestQuestionnaireStatusViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestQuestionnaireStatusViewSet, self).setUp()
        self.url_list = reverse('valuesets:QuestionnaireStatus-list')
        self.url_detail = 'valuesets:QuestionnaireStatus-detail'
        self.model = QuestionnaireStatus
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestReactionEventCertaintyViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestReactionEventCertaintyViewSet, self).setUp()
        self.url_list = reverse('valuesets:ReactionEventCertainty-list')
        self.url_detail = 'valuesets:ReactionEventCertainty-detail'
        self.model = ReactionEventCertainty
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestReactionEventSeverityViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestReactionEventSeverityViewSet, self).setUp()
        self.url_list = reverse('valuesets:ReactionEventSeverity-list')
        self.url_detail = 'valuesets:ReactionEventSeverity-detail'
        self.model = ReactionEventSeverity
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestReasonMedicationGivenCodesViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestReasonMedicationGivenCodesViewSet, self).setUp()
        self.url_list = reverse('valuesets:ReasonMedicationGivenCodes-list')
        self.url_detail = 'valuesets:ReasonMedicationGivenCodes-detail'
        self.model = ReasonMedicationGivenCodes
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestReasonMedicationNotGivenCodesViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestReasonMedicationNotGivenCodesViewSet, self).setUp()
        self.url_list = reverse(
            'valuesets:ReasonMedicationNotGivenCodes-list')
        self.url_detail = 'valuesets:ReasonMedicationNotGivenCodes-detail'
        self.model = ReasonMedicationNotGivenCodes
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestReferenceVersionRulesViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestReferenceVersionRulesViewSet, self).setUp()
        self.url_list = reverse('valuesets:ReferenceVersionRules-list')
        self.url_detail = 'valuesets:ReferenceVersionRules-detail'
        self.model = ReferenceVersionRules
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestReferencerangeMeaningViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestReferencerangeMeaningViewSet, self).setUp()
        self.url_list = reverse('valuesets:ReferencerangeMeaning-list')
        self.url_detail = 'valuesets:ReferencerangeMeaning-detail'
        self.model = ReferencerangeMeaning
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestReferralcategoryViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestReferralcategoryViewSet, self).setUp()
        self.url_list = reverse('valuesets:Referralcategory-list')
        self.url_detail = 'valuesets:Referralcategory-detail'
        self.model = Referralcategory
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestReferralstatusViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestReferralstatusViewSet, self).setUp()
        self.url_list = reverse('valuesets:Referralstatus-list')
        self.url_detail = 'valuesets:Referralstatus-detail'
        self.model = Referralstatus
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestRelationshipViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestRelationshipViewSet, self).setUp()
        self.url_list = reverse('valuesets:Relationship-list')
        self.url_detail = 'valuesets:Relationship-detail'
        self.model = Relationship
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestRemittanceOutcomeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestRemittanceOutcomeViewSet, self).setUp()
        self.url_list = reverse('valuesets:RemittanceOutcome-list')
        self.url_detail = 'valuesets:RemittanceOutcome-detail'
        self.model = RemittanceOutcome
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestRequiredBehaviorViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestRequiredBehaviorViewSet, self).setUp()
        self.url_list = reverse('valuesets:RequiredBehavior-list')
        self.url_detail = 'valuesets:RequiredBehavior-detail'
        self.model = RequiredBehavior
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestResourceAggregationModeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestResourceAggregationModeViewSet, self).setUp()
        self.url_list = reverse('valuesets:ResourceAggregationMode-list')
        self.url_detail = 'valuesets:ResourceAggregationMode-detail'
        self.model = ResourceAggregationMode
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestResourceSlicingRulesViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestResourceSlicingRulesViewSet, self).setUp()
        self.url_list = reverse('valuesets:ResourceSlicingRules-list')
        self.url_detail = 'valuesets:ResourceSlicingRules-detail'
        self.model = ResourceSlicingRules
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestResourceTypeLinkViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestResourceTypeLinkViewSet, self).setUp()
        self.url_list = reverse('valuesets:ResourceTypeLink-list')
        self.url_detail = 'valuesets:ResourceTypeLink-detail'
        self.model = ResourceTypeLink
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestResourceTypesViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestResourceTypesViewSet, self).setUp()
        self.url_list = reverse('valuesets:ResourceTypes-list')
        self.url_detail = 'valuesets:ResourceTypes-detail'
        self.model = ResourceTypes
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestResourceValidationModeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestResourceValidationModeViewSet, self).setUp()
        self.url_list = reverse('valuesets:ResourceValidationMode-list')
        self.url_detail = 'valuesets:ResourceValidationMode-detail'
        self.model = ResourceValidationMode
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestResponseCodeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestResponseCodeViewSet, self).setUp()
        self.url_list = reverse('valuesets:ResponseCode-list')
        self.url_detail = 'valuesets:ResponseCode-detail'
        self.model = ResponseCode
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestRestfulConformanceModeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestRestfulConformanceModeViewSet, self).setUp()
        self.url_list = reverse('valuesets:RestfulConformanceMode-list')
        self.url_detail = 'valuesets:RestfulConformanceMode-detail'
        self.model = RestfulConformanceMode
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestRestfulInteractionViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestRestfulInteractionViewSet, self).setUp()
        self.url_list = reverse('valuesets:RestfulInteraction-list')
        self.url_detail = 'valuesets:RestfulInteraction-detail'
        self.model = RestfulInteraction
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestRestfulSecurityServiceViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestRestfulSecurityServiceViewSet, self).setUp()
        self.url_list = reverse('valuesets:RestfulSecurityService-list')
        self.url_detail = 'valuesets:RestfulSecurityService-detail'
        self.model = RestfulSecurityService
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestRiskProbabilityViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestRiskProbabilityViewSet, self).setUp()
        self.url_list = reverse('valuesets:RiskProbability-list')
        self.url_detail = 'valuesets:RiskProbability-detail'
        self.model = RiskProbability
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestRulesetViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestRulesetViewSet, self).setUp()
        self.url_list = reverse('valuesets:Ruleset-list')
        self.url_detail = 'valuesets:Ruleset-detail'
        self.model = Ruleset
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestSearchEntryModeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestSearchEntryModeViewSet, self).setUp()
        self.url_list = reverse('valuesets:SearchEntryMode-list')
        self.url_detail = 'valuesets:SearchEntryMode-detail'
        self.model = SearchEntryMode
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestSearchModifierCodeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestSearchModifierCodeViewSet, self).setUp()
        self.url_list = reverse('valuesets:SearchModifierCode-list')
        self.url_detail = 'valuesets:SearchModifierCode-detail'
        self.model = SearchModifierCode
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestSearchParamTypeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestSearchParamTypeViewSet, self).setUp()
        self.url_list = reverse('valuesets:SearchParamType-list')
        self.url_detail = 'valuesets:SearchParamType-detail'
        self.model = SearchParamType
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestSearchXpathUsageViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestSearchXpathUsageViewSet, self).setUp()
        self.url_list = reverse('valuesets:SearchXpathUsage-list')
        self.url_detail = 'valuesets:SearchXpathUsage-detail'
        self.model = SearchXpathUsage
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestAuditSourceTypeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestAuditSourceTypeViewSet, self).setUp()
        self.url_list = reverse('valuesets:AuditSourceType-list')
        self.url_detail = 'valuesets:AuditSourceType-detail'
        self.model = AuditSourceType
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestSelectionBehaviorViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestSelectionBehaviorViewSet, self).setUp()
        self.url_list = reverse('valuesets:SelectionBehavior-list')
        self.url_detail = 'valuesets:SelectionBehavior-detail'
        self.model = SelectionBehavior
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestSequenceTypeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestSequenceTypeViewSet, self).setUp()
        self.url_list = reverse('valuesets:SequenceType-list')
        self.url_detail = 'valuesets:SequenceType-detail'
        self.model = SequenceType
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestServiceCategoryViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestServiceCategoryViewSet, self).setUp()
        self.url_list = reverse('valuesets:ServiceCategory-list')
        self.url_detail = 'valuesets:ServiceCategory-detail'
        self.model = ServiceCategory
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestServiceProvisionConditionsViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestServiceProvisionConditionsViewSet, self).setUp()
        self.url_list = reverse('valuesets:ServiceProvisionConditions-list')
        self.url_detail = 'valuesets:ServiceProvisionConditions-detail'
        self.model = ServiceProvisionConditions
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestServiceReferralMethodViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestServiceReferralMethodViewSet, self).setUp()
        self.url_list = reverse('valuesets:ServiceReferralMethod-list')
        self.url_detail = 'valuesets:ServiceReferralMethod-detail'
        self.model = ServiceReferralMethod
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestServiceTypeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestServiceTypeViewSet, self).setUp()
        self.url_list = reverse('valuesets:ServiceType-list')
        self.url_detail = 'valuesets:ServiceType-detail'
        self.model = ServiceType
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestIcd10ProceduresViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestIcd10ProceduresViewSet, self).setUp()
        self.url_list = reverse('valuesets:Icd10Procedures-list')
        self.url_detail = 'valuesets:Icd10Procedures-detail'
        self.model = Icd10Procedures
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestSlotstatusViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestSlotstatusViewSet, self).setUp()
        self.url_list = reverse('valuesets:Slotstatus-list')
        self.url_detail = 'valuesets:Slotstatus-detail'
        self.model = Slotstatus
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestSpecialValuesViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestSpecialValuesViewSet, self).setUp()
        self.url_list = reverse('valuesets:SpecialValues-list')
        self.url_detail = 'valuesets:SpecialValues-detail'
        self.model = SpecialValues
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestSpecimenStatusViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestSpecimenStatusViewSet, self).setUp()
        self.url_list = reverse('valuesets:SpecimenStatus-list')
        self.url_detail = 'valuesets:SpecimenStatus-detail'
        self.model = SpecimenStatus
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestStructureDefinitionKindViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestStructureDefinitionKindViewSet, self).setUp()
        self.url_list = reverse('valuesets:StructureDefinitionKind-list')
        self.url_detail = 'valuesets:StructureDefinitionKind-detail'
        self.model = StructureDefinitionKind
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestSubscriptionChannelTypeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestSubscriptionChannelTypeViewSet, self).setUp()
        self.url_list = reverse('valuesets:SubscriptionChannelType-list')
        self.url_detail = 'valuesets:SubscriptionChannelType-detail'
        self.model = SubscriptionChannelType
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestSubscriptionStatusViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestSubscriptionStatusViewSet, self).setUp()
        self.url_list = reverse('valuesets:SubscriptionStatus-list')
        self.url_detail = 'valuesets:SubscriptionStatus-detail'
        self.model = SubscriptionStatus
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestSubscriptionTagViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestSubscriptionTagViewSet, self).setUp()
        self.url_list = reverse('valuesets:SubscriptionTag-list')
        self.url_detail = 'valuesets:SubscriptionTag-detail'
        self.model = SubscriptionTag
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestSubstanceCategoryViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestSubstanceCategoryViewSet, self).setUp()
        self.url_list = reverse('valuesets:SubstanceCategory-list')
        self.url_detail = 'valuesets:SubstanceCategory-detail'
        self.model = SubstanceCategory
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestSupplydeliveryTypeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestSupplydeliveryTypeViewSet, self).setUp()
        self.url_list = reverse('valuesets:SupplydeliveryType-list')
        self.url_detail = 'valuesets:SupplydeliveryType-detail'
        self.model = SupplydeliveryType
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestSupplyrequestKindViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestSupplyrequestKindViewSet, self).setUp()
        self.url_list = reverse('valuesets:SupplyrequestKind-list')
        self.url_detail = 'valuesets:SupplyrequestKind-detail'
        self.model = SupplyrequestKind
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestSupplydeliveryStatusViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestSupplydeliveryStatusViewSet, self).setUp()
        self.url_list = reverse('valuesets:SupplydeliveryStatus-list')
        self.url_detail = 'valuesets:SupplydeliveryStatus-detail'
        self.model = SupplydeliveryStatus
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestSupplyrequestReasonViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestSupplyrequestReasonViewSet, self).setUp()
        self.url_list = reverse('valuesets:SupplyrequestReason-list')
        self.url_detail = 'valuesets:SupplyrequestReason-detail'
        self.model = SupplyrequestReason
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestSupplyrequestStatusViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestSupplyrequestStatusViewSet, self).setUp()
        self.url_list = reverse('valuesets:SupplyrequestStatus-list')
        self.url_detail = 'valuesets:SupplyrequestStatus-detail'
        self.model = SupplyrequestStatus
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestTaskPerformerTypeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestTaskPerformerTypeViewSet, self).setUp()
        self.url_list = reverse('valuesets:TaskPerformerType-list')
        self.url_detail = 'valuesets:TaskPerformerType-detail'
        self.model = TaskPerformerType
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestTaskPriorityViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestTaskPriorityViewSet, self).setUp()
        self.url_list = reverse('valuesets:TaskPriority-list')
        self.url_detail = 'valuesets:TaskPriority-detail'
        self.model = TaskPriority
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestTaskStageViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestTaskStageViewSet, self).setUp()
        self.url_list = reverse('valuesets:TaskStage-list')
        self.url_detail = 'valuesets:TaskStage-detail'
        self.model = TaskStage
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestTaskStatusViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestTaskStatusViewSet, self).setUp()
        self.url_list = reverse('valuesets:TaskStatus-list')
        self.url_detail = 'valuesets:TaskStatus-detail'
        self.model = TaskStatus
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestTestscriptOperationCodesViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestTestscriptOperationCodesViewSet, self).setUp()
        self.url_list = reverse('valuesets:TestscriptOperationCodes-list')
        self.url_detail = 'valuesets:TestscriptOperationCodes-detail'
        self.model = TestscriptOperationCodes
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestTestscriptProfileDestinationTypesViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestTestscriptProfileDestinationTypesViewSet, self).setUp()
        self.url_list = reverse(
            'valuesets:TestscriptProfileDestinationTypes-list')
        self.url_detail = (
            'valuesets:TestscriptProfileDestinationTypes-detail')
        self.model = TestscriptProfileDestinationTypes
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestTestscriptProfileOriginTypesViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestTestscriptProfileOriginTypesViewSet, self).setUp()
        self.url_list = reverse(
            'valuesets:TestscriptProfileOriginTypes-list')
        self.url_detail = 'valuesets:TestscriptProfileOriginTypes-detail'
        self.model = TestscriptProfileOriginTypes
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestTransactionModeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestTransactionModeViewSet, self).setUp()
        self.url_list = reverse('valuesets:TransactionMode-list')
        self.url_detail = 'valuesets:TransactionMode-detail'
        self.model = TransactionMode
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestTriggerTypeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestTriggerTypeViewSet, self).setUp()
        self.url_list = reverse('valuesets:TriggerType-list')
        self.url_detail = 'valuesets:TriggerType-detail'
        self.model = TriggerType
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestTypeDerivationRuleViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestTypeDerivationRuleViewSet, self).setUp()
        self.url_list = reverse('valuesets:TypeDerivationRule-list')
        self.url_detail = 'valuesets:TypeDerivationRule-detail'
        self.model = TypeDerivationRule
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestUnknownContentCodeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestUnknownContentCodeViewSet, self).setUp()
        self.url_list = reverse('valuesets:UnknownContentCode-list')
        self.url_detail = 'valuesets:UnknownContentCode-detail'
        self.model = UnknownContentCode
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestVaccinationProtocolDoseStatusViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestVaccinationProtocolDoseStatusViewSet, self).setUp()
        self.url_list = reverse(
            'valuesets:VaccinationProtocolDoseStatus-list')
        self.url_detail = 'valuesets:VaccinationProtocolDoseStatus-detail'
        self.model = VaccinationProtocolDoseStatus
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestVaccinationProtocolDoseStatusReasonViewSet(
        APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestVaccinationProtocolDoseStatusReasonViewSet, self).setUp()
        self.url_list = reverse(
            'valuesets:VaccinationProtocolDoseStatusReason-list')
        self.url_detail = (
            'valuesets:VaccinationProtocolDoseStatusReason-detail')
        self.model = VaccinationProtocolDoseStatusReason
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestVariantStateViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestVariantStateViewSet, self).setUp()
        self.url_list = reverse('valuesets:VariantState-list')
        self.url_detail = 'valuesets:VariantState-detail'
        self.model = VariantState
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestVersioningPolicyViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestVersioningPolicyViewSet, self).setUp()
        self.url_list = reverse('valuesets:VersioningPolicy-list')
        self.url_detail = 'valuesets:VersioningPolicy-detail'
        self.model = VersioningPolicy
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestVisionBaseCodesViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestVisionBaseCodesViewSet, self).setUp()
        self.url_list = reverse('valuesets:VisionBaseCodes-list')
        self.url_detail = 'valuesets:VisionBaseCodes-detail'
        self.model = VisionBaseCodes
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestVisionEyeCodesViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestVisionEyeCodesViewSet, self).setUp()
        self.url_list = reverse('valuesets:VisionEyeCodes-list')
        self.url_detail = 'valuesets:VisionEyeCodes-detail'
        self.model = VisionEyeCodes
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestXdsRelationshipTypeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestXdsRelationshipTypeViewSet, self).setUp()
        self.url_list = reverse('valuesets:XdsRelationshipType-list')
        self.url_detail = 'valuesets:XdsRelationshipType-detail'
        self.model = XdsRelationshipType
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestAcknowledgementconditionViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestAcknowledgementconditionViewSet, self).setUp()
        self.url_list = reverse('valuesets:Acknowledgementcondition-list')
        self.url_detail = 'valuesets:Acknowledgementcondition-detail'
        self.model = Acknowledgementcondition
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestAcknowledgementdetailcodeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestAcknowledgementdetailcodeViewSet, self).setUp()
        self.url_list = reverse('valuesets:Acknowledgementdetailcode-list')
        self.url_detail = 'valuesets:Acknowledgementdetailcode-detail'
        self.model = Acknowledgementdetailcode
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestAcknowledgementdetailtypeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestAcknowledgementdetailtypeViewSet, self).setUp()
        self.url_list = reverse('valuesets:Acknowledgementdetailtype-list')
        self.url_detail = 'valuesets:Acknowledgementdetailtype-detail'
        self.model = Acknowledgementdetailtype
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestAcknowledgementtypeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestAcknowledgementtypeViewSet, self).setUp()
        self.url_list = reverse('valuesets:Acknowledgementtype-list')
        self.url_detail = 'valuesets:Acknowledgementtype-detail'
        self.model = Acknowledgementtype
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestActclassViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestActclassViewSet, self).setUp()
        self.url_list = reverse('valuesets:Actclass-list')
        self.url_detail = 'valuesets:Actclass-detail'
        self.model = Actclass
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestActcodeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestActcodeViewSet, self).setUp()
        self.url_list = reverse('valuesets:Actcode-list')
        self.url_detail = 'valuesets:Actcode-detail'
        self.model = Actcode
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestActexposurelevelcodeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestActexposurelevelcodeViewSet, self).setUp()
        self.url_list = reverse('valuesets:Actexposurelevelcode-list')
        self.url_detail = 'valuesets:Actexposurelevelcode-detail'
        self.model = Actexposurelevelcode
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestActinvoiceelementmodifierViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestActinvoiceelementmodifierViewSet, self).setUp()
        self.url_list = reverse('valuesets:Actinvoiceelementmodifier-list')
        self.url_detail = 'valuesets:Actinvoiceelementmodifier-detail'
        self.model = Actinvoiceelementmodifier
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestActmoodViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestActmoodViewSet, self).setUp()
        self.url_list = reverse('valuesets:Actmood-list')
        self.url_detail = 'valuesets:Actmood-detail'
        self.model = Actmood
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestActpriorityViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestActpriorityViewSet, self).setUp()
        self.url_list = reverse('valuesets:Actpriority-list')
        self.url_detail = 'valuesets:Actpriority-detail'
        self.model = Actpriority
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestActreasonViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestActreasonViewSet, self).setUp()
        self.url_list = reverse('valuesets:Actreason-list')
        self.url_detail = 'valuesets:Actreason-detail'
        self.model = Actreason
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestActrelationshipcheckpointViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestActrelationshipcheckpointViewSet, self).setUp()
        self.url_list = reverse('valuesets:Actrelationshipcheckpoint-list')
        self.url_detail = 'valuesets:Actrelationshipcheckpoint-detail'
        self.model = Actrelationshipcheckpoint
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestActrelationshipjoinViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestActrelationshipjoinViewSet, self).setUp()
        self.url_list = reverse('valuesets:Actrelationshipjoin-list')
        self.url_detail = 'valuesets:Actrelationshipjoin-detail'
        self.model = Actrelationshipjoin
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestActrelationshipsplitViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestActrelationshipsplitViewSet, self).setUp()
        self.url_list = reverse('valuesets:Actrelationshipsplit-list')
        self.url_detail = 'valuesets:Actrelationshipsplit-detail'
        self.model = Actrelationshipsplit
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestActrelationshipsubsetViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestActrelationshipsubsetViewSet, self).setUp()
        self.url_list = reverse('valuesets:Actrelationshipsubset-list')
        self.url_detail = 'valuesets:Actrelationshipsubset-detail'
        self.model = Actrelationshipsubset
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestActrelationshiptypeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestActrelationshiptypeViewSet, self).setUp()
        self.url_list = reverse('valuesets:Actrelationshiptype-list')
        self.url_detail = 'valuesets:Actrelationshiptype-detail'
        self.model = Actrelationshiptype
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestActsiteViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestActsiteViewSet, self).setUp()
        self.url_list = reverse('valuesets:Actsite-list')
        self.url_detail = 'valuesets:Actsite-detail'
        self.model = Actsite
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestActstatusViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestActstatusViewSet, self).setUp()
        self.url_list = reverse('valuesets:Actstatus-list')
        self.url_detail = 'valuesets:Actstatus-detail'
        self.model = Actstatus
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestActusprivacylawViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestActusprivacylawViewSet, self).setUp()
        self.url_list = reverse('valuesets:Actusprivacylaw-list')
        self.url_detail = 'valuesets:Actusprivacylaw-detail'
        self.model = Actusprivacylaw
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestActuncertaintyViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestActuncertaintyViewSet, self).setUp()
        self.url_list = reverse('valuesets:Actuncertainty-list')
        self.url_detail = 'valuesets:Actuncertainty-detail'
        self.model = Actuncertainty
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestAddressparttypeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestAddressparttypeViewSet, self).setUp()
        self.url_list = reverse('valuesets:Addressparttype-list')
        self.url_detail = 'valuesets:Addressparttype-detail'
        self.model = Addressparttype
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestAmericanindianalaskanativelanguagesViewSet(
        APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestAmericanindianalaskanativelanguagesViewSet, self).setUp()
        self.url_list = reverse(
            'valuesets:Americanindianalaskanativelanguages-list')
        self.url_detail = 'valuesets:Americanindianalaskanativelanguages-detail'
        self.model = Americanindianalaskanativelanguages
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestCalendarViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestCalendarViewSet, self).setUp()
        self.url_list = reverse('valuesets:Calendar-list')
        self.url_detail = 'valuesets:Calendar-detail'
        self.model = Calendar
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestCalendarcycleViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestCalendarcycleViewSet, self).setUp()
        self.url_list = reverse('valuesets:Calendarcycle-list')
        self.url_detail = 'valuesets:Calendarcycle-detail'
        self.model = Calendarcycle
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestCalendartypeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestCalendartypeViewSet, self).setUp()
        self.url_list = reverse('valuesets:Calendartype-list')
        self.url_detail = 'valuesets:Calendartype-detail'
        self.model = Calendartype
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestCharsetViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestCharsetViewSet, self).setUp()
        self.url_list = reverse('valuesets:Charset-list')
        self.url_detail = 'valuesets:Charset-detail'
        self.model = Charset
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestCodingrationaleViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestCodingrationaleViewSet, self).setUp()
        self.url_list = reverse('valuesets:Codingrationale-list')
        self.url_detail = 'valuesets:Codingrationale-detail'
        self.model = Codingrationale
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestCommunicationfunctiontypeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestCommunicationfunctiontypeViewSet, self).setUp()
        self.url_list = reverse('valuesets:Communicationfunctiontype-list')
        self.url_detail = 'valuesets:Communicationfunctiontype-detail'
        self.model = Communicationfunctiontype
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestCompressionalgorithmViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestCompressionalgorithmViewSet, self).setUp()
        self.url_list = reverse('valuesets:Compressionalgorithm-list')
        self.url_detail = 'valuesets:Compressionalgorithm-detail'
        self.model = Compressionalgorithm
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestConfidentialityViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestConfidentialityViewSet, self).setUp()
        self.url_list = reverse('valuesets:Confidentiality-list')
        self.url_detail = 'valuesets:Confidentiality-detail'
        self.model = Confidentiality
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestContainercapViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestContainercapViewSet, self).setUp()
        self.url_list = reverse('valuesets:Containercap-list')
        self.url_detail = 'valuesets:Containercap-detail'
        self.model = Containercap
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestContainerseparatorViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestContainerseparatorViewSet, self).setUp()
        self.url_list = reverse('valuesets:Containerseparator-list')
        self.url_detail = 'valuesets:Containerseparator-detail'
        self.model = Containerseparator
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestContentprocessingmodeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestContentprocessingmodeViewSet, self).setUp()
        self.url_list = reverse('valuesets:Contentprocessingmode-list')
        self.url_detail = 'valuesets:Contentprocessingmode-detail'
        self.model = Contentprocessingmode
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestContextcontrolViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestContextcontrolViewSet, self).setUp()
        self.url_list = reverse('valuesets:Contextcontrol-list')
        self.url_detail = 'valuesets:Contextcontrol-detail'
        self.model = Contextcontrol
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestDataoperationViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestDataoperationViewSet, self).setUp()
        self.url_list = reverse('valuesets:Dataoperation-list')
        self.url_detail = 'valuesets:Dataoperation-detail'
        self.model = Dataoperation
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestDevicealertlevelViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestDevicealertlevelViewSet, self).setUp()
        self.url_list = reverse('valuesets:Devicealertlevel-list')
        self.url_detail = 'valuesets:Devicealertlevel-detail'
        self.model = Devicealertlevel
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestDocumentcompletionViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestDocumentcompletionViewSet, self).setUp()
        self.url_list = reverse('valuesets:Documentcompletion-list')
        self.url_detail = 'valuesets:Documentcompletion-detail'
        self.model = Documentcompletion
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestDocumentstorageViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestDocumentstorageViewSet, self).setUp()
        self.url_list = reverse('valuesets:Documentstorage-list')
        self.url_detail = 'valuesets:Documentstorage-detail'
        self.model = Documentstorage
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestEducationlevelViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestEducationlevelViewSet, self).setUp()
        self.url_list = reverse('valuesets:Educationlevel-list')
        self.url_detail = 'valuesets:Educationlevel-detail'
        self.model = Educationlevel
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestEmployeejobclassViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestEmployeejobclassViewSet, self).setUp()
        self.url_list = reverse('valuesets:Employeejobclass-list')
        self.url_detail = 'valuesets:Employeejobclass-detail'
        self.model = Employeejobclass
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestEncounteradmissionsourceViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestEncounteradmissionsourceViewSet, self).setUp()
        self.url_list = reverse('valuesets:Encounteradmissionsource-list')
        self.url_detail = 'valuesets:Encounteradmissionsource-detail'
        self.model = Encounteradmissionsource
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestEncounterspecialcourtesyViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestEncounterspecialcourtesyViewSet, self).setUp()
        self.url_list = reverse('valuesets:Encounterspecialcourtesy-list')
        self.url_detail = 'valuesets:Encounterspecialcourtesy-detail'
        self.model = Encounterspecialcourtesy
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestEntityclassViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestEntityclassViewSet, self).setUp()
        self.url_list = reverse('valuesets:Entityclass-list')
        self.url_detail = 'valuesets:Entityclass-detail'
        self.model = Entityclass
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestEntitycodeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestEntitycodeViewSet, self).setUp()
        self.url_list = reverse('valuesets:Entitycode-list')
        self.url_detail = 'valuesets:Entitycode-detail'
        self.model = Entitycode
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestEntitydeterminerViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestEntitydeterminerViewSet, self).setUp()
        self.url_list = reverse('valuesets:Entitydeterminer-list')
        self.url_detail = 'valuesets:Entitydeterminer-detail'
        self.model = Entitydeterminer
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestEntityhandlingViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestEntityhandlingViewSet, self).setUp()
        self.url_list = reverse('valuesets:Entityhandling-list')
        self.url_detail = 'valuesets:Entityhandling-detail'
        self.model = Entityhandling
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestEntitynamepartqualifierViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestEntitynamepartqualifierViewSet, self).setUp()
        self.url_list = reverse('valuesets:Entitynamepartqualifier-list')
        self.url_detail = 'valuesets:Entitynamepartqualifier-detail'
        self.model = Entitynamepartqualifier
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestEntitynamepartqualifierr2ViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestEntitynamepartqualifierr2ViewSet, self).setUp()
        self.url_list = reverse('valuesets:Entitynamepartqualifierr2-list')
        self.url_detail = 'valuesets:Entitynamepartqualifierr2-detail'
        self.model = Entitynamepartqualifierr2
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestEntitynameparttypeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestEntitynameparttypeViewSet, self).setUp()
        self.url_list = reverse('valuesets:Entitynameparttype-list')
        self.url_detail = 'valuesets:Entitynameparttype-detail'
        self.model = Entitynameparttype
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestEntitynameparttyper2ViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestEntitynameparttyper2ViewSet, self).setUp()
        self.url_list = reverse('valuesets:Entitynameparttyper2-list')
        self.url_detail = 'valuesets:Entitynameparttyper2-detail'
        self.model = Entitynameparttyper2
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestEntitynameuseViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestEntitynameuseViewSet, self).setUp()
        self.url_list = reverse('valuesets:Entitynameuse-list')
        self.url_detail = 'valuesets:Entitynameuse-detail'
        self.model = Entitynameuse
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestEntitynameuser2ViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestEntitynameuser2ViewSet, self).setUp()
        self.url_list = reverse('valuesets:Entitynameuser2-list')
        self.url_detail = 'valuesets:Entitynameuser2-detail'
        self.model = Entitynameuser2
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestEntityriskViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestEntityriskViewSet, self).setUp()
        self.url_list = reverse('valuesets:Entityrisk-list')
        self.url_detail = 'valuesets:Entityrisk-detail'
        self.model = Entityrisk
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestEntitystatusViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestEntitystatusViewSet, self).setUp()
        self.url_list = reverse('valuesets:Entitystatus-list')
        self.url_detail = 'valuesets:Entitystatus-detail'
        self.model = Entitystatus
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestEquipmentalertlevelViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestEquipmentalertlevelViewSet, self).setUp()
        self.url_list = reverse('valuesets:Equipmentalertlevel-list')
        self.url_detail = 'valuesets:Equipmentalertlevel-detail'
        self.model = Equipmentalertlevel
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestEthnicityViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestEthnicityViewSet, self).setUp()
        self.url_list = reverse('valuesets:Ethnicity-list')
        self.url_detail = 'valuesets:Ethnicity-detail'
        self.model = Ethnicity
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestExposuremodeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestExposuremodeViewSet, self).setUp()
        self.url_list = reverse('valuesets:Exposuremode-list')
        self.url_detail = 'valuesets:Exposuremode-detail'
        self.model = Exposuremode
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestGtsabbreviationViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestGtsabbreviationViewSet, self).setUp()
        self.url_list = reverse('valuesets:Gtsabbreviation-list')
        self.url_detail = 'valuesets:Gtsabbreviation-detail'
        self.model = Gtsabbreviation
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestGenderstatusViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestGenderstatusViewSet, self).setUp()
        self.url_list = reverse('valuesets:Genderstatus-list')
        self.url_detail = 'valuesets:Genderstatus-detail'
        self.model = Genderstatus
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestHl7updatemodeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestHl7updatemodeViewSet, self).setUp()
        self.url_list = reverse('valuesets:Hl7updatemode-list')
        self.url_detail = 'valuesets:Hl7updatemode-detail'
        self.model = Hl7updatemode
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestHtmllinktypeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestHtmllinktypeViewSet, self).setUp()
        self.url_list = reverse('valuesets:Htmllinktype-list')
        self.url_detail = 'valuesets:Htmllinktype-detail'
        self.model = Htmllinktype
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestIdentifierreliabilityViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestIdentifierreliabilityViewSet, self).setUp()
        self.url_list = reverse('valuesets:Identifierreliability-list')
        self.url_detail = 'valuesets:Identifierreliability-detail'
        self.model = Identifierreliability
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestIdentifierscopeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestIdentifierscopeViewSet, self).setUp()
        self.url_list = reverse('valuesets:Identifierscope-list')
        self.url_detail = 'valuesets:Identifierscope-detail'
        self.model = Identifierscope
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestIntegritycheckalgorithmViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestIntegritycheckalgorithmViewSet, self).setUp()
        self.url_list = reverse('valuesets:Integritycheckalgorithm-list')
        self.url_detail = 'valuesets:Integritycheckalgorithm-detail'
        self.model = Integritycheckalgorithm
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestLanguageabilitymodeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestLanguageabilitymodeViewSet, self).setUp()
        self.url_list = reverse('valuesets:Languageabilitymode-list')
        self.url_detail = 'valuesets:Languageabilitymode-detail'
        self.model = Languageabilitymode
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestLanguageabilityproficiencyViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestLanguageabilityproficiencyViewSet, self).setUp()
        self.url_list = reverse('valuesets:Languageabilityproficiency-list')
        self.url_detail = 'valuesets:Languageabilityproficiency-detail'
        self.model = Languageabilityproficiency
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestLivingarrangementViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestLivingarrangementViewSet, self).setUp()
        self.url_list = reverse('valuesets:Livingarrangement-list')
        self.url_detail = 'valuesets:Livingarrangement-detail'
        self.model = Livingarrangement
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestLocalmarkupignoreViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestLocalmarkupignoreViewSet, self).setUp()
        self.url_list = reverse('valuesets:Localmarkupignore-list')
        self.url_detail = 'valuesets:Localmarkupignore-detail'
        self.model = Localmarkupignore
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestLocalremotecontrolstateViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestLocalremotecontrolstateViewSet, self).setUp()
        self.url_list = reverse('valuesets:Localremotecontrolstate-list')
        self.url_detail = 'valuesets:Localremotecontrolstate-detail'
        self.model = Localremotecontrolstate
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestManagedparticipationstatusViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestManagedparticipationstatusViewSet, self).setUp()
        self.url_list = reverse('valuesets:Managedparticipationstatus-list')
        self.url_detail = 'valuesets:Managedparticipationstatus-detail'
        self.model = Managedparticipationstatus
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestMaprelationshipViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestMaprelationshipViewSet, self).setUp()
        self.url_list = reverse('valuesets:Maprelationship-list')
        self.url_detail = 'valuesets:Maprelationship-detail'
        self.model = Maprelationship
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestMessagewaitingpriorityViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestMessagewaitingpriorityViewSet, self).setUp()
        self.url_list = reverse('valuesets:Messagewaitingpriority-list')
        self.url_detail = 'valuesets:Messagewaitingpriority-detail'
        self.model = Messagewaitingpriority
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestModifyindicatorViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestModifyindicatorViewSet, self).setUp()
        self.url_list = reverse('valuesets:Modifyindicator-list')
        self.url_detail = 'valuesets:Modifyindicator-detail'
        self.model = Modifyindicator
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestNullflavorViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestNullflavorViewSet, self).setUp()
        self.url_list = reverse('valuesets:Nullflavor-list')
        self.url_detail = 'valuesets:Nullflavor-detail'
        self.model = Nullflavor
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestObservationinterpretationViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestObservationinterpretationViewSet, self).setUp()
        self.url_list = reverse('valuesets:Observationinterpretation-list')
        self.url_detail = 'valuesets:Observationinterpretation-detail'
        self.model = Observationinterpretation
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestObservationmethodViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestObservationmethodViewSet, self).setUp()
        self.url_list = reverse('valuesets:Observationmethod-list')
        self.url_detail = 'valuesets:Observationmethod-detail'
        self.model = Observationmethod
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestObservationvalueViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestObservationvalueViewSet, self).setUp()
        self.url_list = reverse('valuesets:Observationvalue-list')
        self.url_detail = 'valuesets:Observationvalue-detail'
        self.model = Observationvalue
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestParticipationfunctionViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestParticipationfunctionViewSet, self).setUp()
        self.url_list = reverse('valuesets:Participationfunction-list')
        self.url_detail = 'valuesets:Participationfunction-detail'
        self.model = Participationfunction
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestParticipationmodeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestParticipationmodeViewSet, self).setUp()
        self.url_list = reverse('valuesets:Participationmode-list')
        self.url_detail = 'valuesets:Participationmode-detail'
        self.model = Participationmode
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestParticipationsignatureViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestParticipationsignatureViewSet, self).setUp()
        self.url_list = reverse('valuesets:Participationsignature-list')
        self.url_detail = 'valuesets:Participationsignature-detail'
        self.model = Participationsignature
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestParticipationtypeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestParticipationtypeViewSet, self).setUp()
        self.url_list = reverse('valuesets:Participationtype-list')
        self.url_detail = 'valuesets:Participationtype-detail'
        self.model = Participationtype
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestPatientimportanceViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestPatientimportanceViewSet, self).setUp()
        self.url_list = reverse('valuesets:Patientimportance-list')
        self.url_detail = 'valuesets:Patientimportance-detail'
        self.model = Patientimportance
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestPaymenttermsViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestPaymenttermsViewSet, self).setUp()
        self.url_list = reverse('valuesets:Paymentterms-list')
        self.url_detail = 'valuesets:Paymentterms-detail'
        self.model = Paymentterms
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestPersondisabilitytypeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestPersondisabilitytypeViewSet, self).setUp()
        self.url_list = reverse('valuesets:Persondisabilitytype-list')
        self.url_detail = 'valuesets:Persondisabilitytype-detail'
        self.model = Persondisabilitytype
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestProbabilitydistributiontypeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestProbabilitydistributiontypeViewSet, self).setUp()
        self.url_list = reverse('valuesets:Probabilitydistributiontype-list')
        self.url_detail = 'valuesets:Probabilitydistributiontype-detail'
        self.model = Probabilitydistributiontype
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestProcessingidViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestProcessingidViewSet, self).setUp()
        self.url_list = reverse('valuesets:Processingid-list')
        self.url_detail = 'valuesets:Processingid-detail'
        self.model = Processingid
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestProcessingmodeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestProcessingmodeViewSet, self).setUp()
        self.url_list = reverse('valuesets:Processingmode-list')
        self.url_detail = 'valuesets:Processingmode-detail'
        self.model = Processingmode
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestQueryparametervalueViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestQueryparametervalueViewSet, self).setUp()
        self.url_list = reverse('valuesets:Queryparametervalue-list')
        self.url_detail = 'valuesets:Queryparametervalue-detail'
        self.model = Queryparametervalue
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestQuerypriorityViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestQuerypriorityViewSet, self).setUp()
        self.url_list = reverse('valuesets:Querypriority-list')
        self.url_detail = 'valuesets:Querypriority-detail'
        self.model = Querypriority
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestQueryrequestlimitViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestQueryrequestlimitViewSet, self).setUp()
        self.url_list = reverse('valuesets:Queryrequestlimit-list')
        self.url_detail = 'valuesets:Queryrequestlimit-detail'
        self.model = Queryrequestlimit
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestQueryresponseViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestQueryresponseViewSet, self).setUp()
        self.url_list = reverse('valuesets:Queryresponse-list')
        self.url_detail = 'valuesets:Queryresponse-detail'
        self.model = Queryresponse
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestQuerystatuscodeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestQuerystatuscodeViewSet, self).setUp()
        self.url_list = reverse('valuesets:Querystatuscode-list')
        self.url_detail = 'valuesets:Querystatuscode-detail'
        self.model = Querystatuscode
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestRaceViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestRaceViewSet, self).setUp()
        self.url_list = reverse('valuesets:Race-list')
        self.url_detail = 'valuesets:Race-detail'
        self.model = Race
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestRelationaloperatorViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestRelationaloperatorViewSet, self).setUp()
        self.url_list = reverse('valuesets:Relationaloperator-list')
        self.url_detail = 'valuesets:Relationaloperator-detail'
        self.model = Relationaloperator
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestRelationshipconjunctionViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestRelationshipconjunctionViewSet, self).setUp()
        self.url_list = reverse('valuesets:Relationshipconjunction-list')
        self.url_detail = 'valuesets:Relationshipconjunction-detail'
        self.model = Relationshipconjunction
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestReligiousaffiliationViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestReligiousaffiliationViewSet, self).setUp()
        self.url_list = reverse('valuesets:Religiousaffiliation-list')
        self.url_detail = 'valuesets:Religiousaffiliation-detail'
        self.model = Religiousaffiliation
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestResponselevelViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestResponselevelViewSet, self).setUp()
        self.url_list = reverse('valuesets:Responselevel-list')
        self.url_detail = 'valuesets:Responselevel-detail'
        self.model = Responselevel
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestResponsemodalityViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestResponsemodalityViewSet, self).setUp()
        self.url_list = reverse('valuesets:Responsemodality-list')
        self.url_detail = 'valuesets:Responsemodality-detail'
        self.model = Responsemodality
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestResponsemodeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestResponsemodeViewSet, self).setUp()
        self.url_list = reverse('valuesets:Responsemode-list')
        self.url_detail = 'valuesets:Responsemode-detail'
        self.model = Responsemode
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestRoleclassViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestRoleclassViewSet, self).setUp()
        self.url_list = reverse('valuesets:Roleclass-list')
        self.url_detail = 'valuesets:Roleclass-detail'
        self.model = Roleclass
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestRolecodeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestRolecodeViewSet, self).setUp()
        self.url_list = reverse('valuesets:Rolecode-list')
        self.url_detail = 'valuesets:Rolecode-detail'
        self.model = Rolecode
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestRolelinkstatusViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestRolelinkstatusViewSet, self).setUp()
        self.url_list = reverse('valuesets:Rolelinkstatus-list')
        self.url_detail = 'valuesets:Rolelinkstatus-detail'
        self.model = Rolelinkstatus
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestRolelinktypeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestRolelinktypeViewSet, self).setUp()
        self.url_list = reverse('valuesets:Rolelinktype-list')
        self.url_detail = 'valuesets:Rolelinktype-detail'
        self.model = Rolelinktype
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestRolestatusViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestRolestatusViewSet, self).setUp()
        self.url_list = reverse('valuesets:Rolestatus-list')
        self.url_detail = 'valuesets:Rolestatus-detail'
        self.model = Rolestatus
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestRouteofadministrationViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestRouteofadministrationViewSet, self).setUp()
        self.url_list = reverse('valuesets:Routeofadministration-list')
        self.url_detail = 'valuesets:Routeofadministration-detail'
        self.model = Routeofadministration
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestSequencingViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestSequencingViewSet, self).setUp()
        self.url_list = reverse('valuesets:Sequencing-list')
        self.url_detail = 'valuesets:Sequencing-detail'
        self.model = Sequencing
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestSetoperatorViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestSetoperatorViewSet, self).setUp()
        self.url_list = reverse('valuesets:Setoperator-list')
        self.url_detail = 'valuesets:Setoperator-detail'
        self.model = Setoperator
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestSpecimentypeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestSpecimentypeViewSet, self).setUp()
        self.url_list = reverse('valuesets:Specimentype-list')
        self.url_detail = 'valuesets:Specimentype-detail'
        self.model = Specimentype
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestSubstitutionconditionViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestSubstitutionconditionViewSet, self).setUp()
        self.url_list = reverse('valuesets:Substitutioncondition-list')
        self.url_detail = 'valuesets:Substitutioncondition-detail'
        self.model = Substitutioncondition
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestTablecellhorizontalalignViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestTablecellhorizontalalignViewSet, self).setUp()
        self.url_list = reverse('valuesets:Tablecellhorizontalalign-list')
        self.url_detail = 'valuesets:Tablecellhorizontalalign-detail'
        self.model = Tablecellhorizontalalign
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestTablecellscopeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestTablecellscopeViewSet, self).setUp()
        self.url_list = reverse('valuesets:Tablecellscope-list')
        self.url_detail = 'valuesets:Tablecellscope-detail'
        self.model = Tablecellscope
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestTablecellverticalalignViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestTablecellverticalalignViewSet, self).setUp()
        self.url_list = reverse('valuesets:Tablecellverticalalign-list')
        self.url_detail = 'valuesets:Tablecellverticalalign-detail'
        self.model = Tablecellverticalalign
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestTableframeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestTableframeViewSet, self).setUp()
        self.url_list = reverse('valuesets:Tableframe-list')
        self.url_detail = 'valuesets:Tableframe-detail'
        self.model = Tableframe
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestTablerulesViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestTablerulesViewSet, self).setUp()
        self.url_list = reverse('valuesets:Tablerules-list')
        self.url_detail = 'valuesets:Tablerules-detail'
        self.model = Tablerules
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestTargetawarenessViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestTargetawarenessViewSet, self).setUp()
        self.url_list = reverse('valuesets:Targetawareness-list')
        self.url_detail = 'valuesets:Targetawareness-detail'
        self.model = Targetawareness
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestTelecommunicationcapabilitiesViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestTelecommunicationcapabilitiesViewSet, self).setUp()
        self.url_list = reverse('valuesets:Telecommunicationcapabilities-list')
        self.url_detail = 'valuesets:Telecommunicationcapabilities-detail'
        self.model = Telecommunicationcapabilities
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestTimingeventViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestTimingeventViewSet, self).setUp()
        self.url_list = reverse('valuesets:Timingevent-list')
        self.url_detail = 'valuesets:Timingevent-detail'
        self.model = Timingevent
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestTransmissionrelationshiptypecodeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestTransmissionrelationshiptypecodeViewSet, self).setUp()
        self.url_list = reverse(
            'valuesets:Transmissionrelationshiptypecode-list')
        self.url_detail = 'valuesets:Transmissionrelationshiptypecode-detail'
        self.model = Transmissionrelationshiptypecode
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestTribalentityusViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestTribalentityusViewSet, self).setUp()
        self.url_list = reverse('valuesets:Tribalentityus-list')
        self.url_detail = 'valuesets:Tribalentityus-detail'
        self.model = Tribalentityus
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestVaccinemanufacturerViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestVaccinemanufacturerViewSet, self).setUp()
        self.url_list = reverse('valuesets:Vaccinemanufacturer-list')
        self.url_detail = 'valuesets:Vaccinemanufacturer-detail'
        self.model = Vaccinemanufacturer
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestHl7realmViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestHl7realmViewSet, self).setUp()
        self.url_list = reverse('valuesets:Hl7realm-list')
        self.url_detail = 'valuesets:Hl7realm-detail'
        self.model = Hl7realm
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestHl7v3conformanceViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestHl7v3conformanceViewSet, self).setUp()
        self.url_list = reverse('valuesets:Hl7v3conformance-list')
        self.url_detail = 'valuesets:Hl7v3conformance-detail'
        self.model = Hl7v3conformance
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestOrderabledrugformViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestOrderabledrugformViewSet, self).setUp()
        self.url_list = reverse('valuesets:Orderabledrugform-list')
        self.url_detail = 'valuesets:Orderabledrugform-detail'
        self.model = Orderabledrugform
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestSubstanceadminsubstitutionViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestSubstanceadminsubstitutionViewSet, self).setUp()
        self.url_list = reverse('valuesets:Substanceadminsubstitution-list')
        self.url_detail = 'valuesets:Substanceadminsubstitution-detail'
        self.model = Substanceadminsubstitution
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'
