from django.core.urlresolvers import reverse

from rest_framework.test import APITestCase

from fhir_valuesets.valuesets.models.generated_models import *  # noqa
from tests.test_valueset_views import BaseViewsTest


class TestExampleViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestExampleViewSet, self).setUp()
        self.url_list = reverse('valuesets:example-list')
        self.url_detail = 'valuesets:example-detail'
        self.model = Example
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestSurfaceViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestSurfaceViewSet, self).setUp()
        self.url_list = reverse('valuesets:surface-list')
        self.url_detail = 'valuesets:surface-detail'
        self.model = Surface
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestLoinc480020AnswerlistViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestLoinc480020AnswerlistViewSet, self).setUp()
        self.url_list = reverse('valuesets:LOINC_48002_0_answerlist-list')
        self.url_detail = 'valuesets:LOINC_48002_0_answerlist-detail'
        self.model = Loinc480020Answerlist
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestLoinc480194AnswerlistViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestLoinc480194AnswerlistViewSet, self).setUp()
        self.url_list = reverse('valuesets:LOINC_48019_4_answerlist-list')
        self.url_detail = 'valuesets:LOINC_48019_4_answerlist-detail'
        self.model = Loinc480194Answerlist
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestLoinc530345AnswerlistViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestLoinc530345AnswerlistViewSet, self).setUp()
        self.url_list = reverse('valuesets:LOINC_53034_5_answerlist-list')
        self.url_detail = 'valuesets:LOINC_53034_5_answerlist-detail'
        self.model = Loinc530345Answerlist
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestAbstractTypesViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestAbstractTypesViewSet, self).setUp()
        self.url_list = reverse('valuesets:abstract_types-list')
        self.url_detail = 'valuesets:abstract_types-detail'
        self.model = AbstractTypes
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestAccountStatusViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestAccountStatusViewSet, self).setUp()
        self.url_list = reverse('valuesets:account_status-list')
        self.url_detail = 'valuesets:account_status-detail'
        self.model = AccountStatus
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestActionBehaviorTypeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestActionBehaviorTypeViewSet, self).setUp()
        self.url_list = reverse('valuesets:action_behavior_type-list')
        self.url_detail = 'valuesets:action_behavior_type-detail'
        self.model = ActionBehaviorType
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestActionCardinalityBehaviorViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestActionCardinalityBehaviorViewSet, self).setUp()
        self.url_list = reverse('valuesets:action_cardinality_behavior-list')
        self.url_detail = 'valuesets:action_cardinality_behavior-detail'
        self.model = ActionCardinalityBehavior
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestActionGroupingBehaviorViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestActionGroupingBehaviorViewSet, self).setUp()
        self.url_list = reverse('valuesets:action_grouping_behavior-list')
        self.url_detail = 'valuesets:action_grouping_behavior-detail'
        self.model = ActionGroupingBehavior
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestActionParticipantTypeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestActionParticipantTypeViewSet, self).setUp()
        self.url_list = reverse('valuesets:action_participant_type-list')
        self.url_detail = 'valuesets:action_participant_type-detail'
        self.model = ActionParticipantType
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestActionPrecheckBehaviorViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestActionPrecheckBehaviorViewSet, self).setUp()
        self.url_list = reverse('valuesets:action_precheck_behavior-list')
        self.url_detail = 'valuesets:action_precheck_behavior-detail'
        self.model = ActionPrecheckBehavior
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestActionRelationshipAnchorViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestActionRelationshipAnchorViewSet, self).setUp()
        self.url_list = reverse('valuesets:action_relationship_anchor-list')
        self.url_detail = 'valuesets:action_relationship_anchor-detail'
        self.model = ActionRelationshipAnchor
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestActionRelationshipTypeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestActionRelationshipTypeViewSet, self).setUp()
        self.url_list = reverse('valuesets:action_relationship_type-list')
        self.url_detail = 'valuesets:action_relationship_type-detail'
        self.model = ActionRelationshipType
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestActionRequiredBehaviorViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestActionRequiredBehaviorViewSet, self).setUp()
        self.url_list = reverse('valuesets:action_required_behavior-list')
        self.url_detail = 'valuesets:action_required_behavior-detail'
        self.model = ActionRequiredBehavior
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestActionSelectionBehaviorViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestActionSelectionBehaviorViewSet, self).setUp()
        self.url_list = reverse('valuesets:action_selection_behavior-list')
        self.url_detail = 'valuesets:action_selection_behavior-detail'
        self.model = ActionSelectionBehavior
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestActionTypeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestActionTypeViewSet, self).setUp()
        self.url_list = reverse('valuesets:action_type-list')
        self.url_detail = 'valuesets:action_type-detail'
        self.model = ActionType
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestActionlistViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestActionlistViewSet, self).setUp()
        self.url_list = reverse('valuesets:actionlist-list')
        self.url_detail = 'valuesets:actionlist-detail'
        self.model = Actionlist
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestActivityDefinitionCategoryViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestActivityDefinitionCategoryViewSet, self).setUp()
        self.url_list = reverse('valuesets:activity_definition_category-list')
        self.url_detail = 'valuesets:activity_definition_category-detail'
        self.model = ActivityDefinitionCategory
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestActivityParticipantTypeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestActivityParticipantTypeViewSet, self).setUp()
        self.url_list = reverse('valuesets:activity_participant_type-list')
        self.url_detail = 'valuesets:activity_participant_type-detail'
        self.model = ActivityParticipantType
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestAdditionalmaterialsViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestAdditionalmaterialsViewSet, self).setUp()
        self.url_list = reverse('valuesets:additionalmaterials-list')
        self.url_detail = 'valuesets:additionalmaterials-detail'
        self.model = Additionalmaterials
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestAddressTypeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestAddressTypeViewSet, self).setUp()
        self.url_list = reverse('valuesets:address_type-list')
        self.url_detail = 'valuesets:address_type-detail'
        self.model = AddressType
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestAddressUseViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestAddressUseViewSet, self).setUp()
        self.url_list = reverse('valuesets:address_use-list')
        self.url_detail = 'valuesets:address_use-detail'
        self.model = AddressUse
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestAdjudicationViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestAdjudicationViewSet, self).setUp()
        self.url_list = reverse('valuesets:adjudication-list')
        self.url_detail = 'valuesets:adjudication-detail'
        self.model = Adjudication
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestAdjudicationErrorViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestAdjudicationErrorViewSet, self).setUp()
        self.url_list = reverse('valuesets:adjudication_error-list')
        self.url_detail = 'valuesets:adjudication_error-detail'
        self.model = AdjudicationError
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestAdjudicationReasonViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestAdjudicationReasonViewSet, self).setUp()
        self.url_list = reverse('valuesets:adjudication_reason-list')
        self.url_detail = 'valuesets:adjudication_reason-detail'
        self.model = AdjudicationReason
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestAdministrativeGenderViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestAdministrativeGenderViewSet, self).setUp()
        self.url_list = reverse('valuesets:administrative_gender-list')
        self.url_detail = 'valuesets:administrative_gender-detail'
        self.model = AdministrativeGender
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestEncounterAdmitSourceViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestEncounterAdmitSourceViewSet, self).setUp()
        self.url_list = reverse('valuesets:encounter_admit_source-list')
        self.url_detail = 'valuesets:encounter_admit_source-detail'
        self.model = EncounterAdmitSource
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestAllergyIntoleranceCategoryViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestAllergyIntoleranceCategoryViewSet, self).setUp()
        self.url_list = reverse('valuesets:allergy_intolerance_category-list')
        self.url_detail = 'valuesets:allergy_intolerance_category-detail'
        self.model = AllergyIntoleranceCategory
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestAllergyIntoleranceCriticalityViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestAllergyIntoleranceCriticalityViewSet, self).setUp()
        self.url_list = reverse(
            'valuesets:allergy_intolerance_criticality-list')
        self.url_detail = 'valuesets:allergy_intolerance_criticality-detail'
        self.model = AllergyIntoleranceCriticality
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestAllergyIntoleranceStatusViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestAllergyIntoleranceStatusViewSet, self).setUp()
        self.url_list = reverse('valuesets:allergy_intolerance_status-list')
        self.url_detail = 'valuesets:allergy_intolerance_status-detail'
        self.model = AllergyIntoleranceStatus
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestAllergyIntoleranceTypeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestAllergyIntoleranceTypeViewSet, self).setUp()
        self.url_list = reverse('valuesets:allergy_intolerance_type-list')
        self.url_detail = 'valuesets:allergy_intolerance_type-detail'
        self.model = AllergyIntoleranceType
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestAnimalBreedsViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestAnimalBreedsViewSet, self).setUp()
        self.url_list = reverse('valuesets:animal_breeds-list')
        self.url_detail = 'valuesets:animal_breeds-detail'
        self.model = AnimalBreeds
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestAnimalGenderstatusViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestAnimalGenderstatusViewSet, self).setUp()
        self.url_list = reverse('valuesets:animal_genderstatus-list')
        self.url_detail = 'valuesets:animal_genderstatus-detail'
        self.model = AnimalGenderstatus
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestAnimalSpeciesViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestAnimalSpeciesViewSet, self).setUp()
        self.url_list = reverse('valuesets:animal_species-list')
        self.url_detail = 'valuesets:animal_species-detail'
        self.model = AnimalSpecies
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestAppointmentstatusViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestAppointmentstatusViewSet, self).setUp()
        self.url_list = reverse('valuesets:appointmentstatus-list')
        self.url_detail = 'valuesets:appointmentstatus-detail'
        self.model = Appointmentstatus
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestAssertDirectionCodesViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestAssertDirectionCodesViewSet, self).setUp()
        self.url_list = reverse('valuesets:assert_direction_codes-list')
        self.url_detail = 'valuesets:assert_direction_codes-detail'
        self.model = AssertDirectionCodes
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestAssertOperatorCodesViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestAssertOperatorCodesViewSet, self).setUp()
        self.url_list = reverse('valuesets:assert_operator_codes-list')
        self.url_detail = 'valuesets:assert_operator_codes-detail'
        self.model = AssertOperatorCodes
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestAssertResponseCodeTypesViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestAssertResponseCodeTypesViewSet, self).setUp()
        self.url_list = reverse('valuesets:assert_response_code_types-list')
        self.url_detail = 'valuesets:assert_response_code_types-detail'
        self.model = AssertResponseCodeTypes
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestAuditEventActionViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestAuditEventActionViewSet, self).setUp()
        self.url_list = reverse('valuesets:audit_event_action-list')
        self.url_detail = 'valuesets:audit_event_action-detail'
        self.model = AuditEventAction
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestAuditEventOutcomeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestAuditEventOutcomeViewSet, self).setUp()
        self.url_list = reverse('valuesets:audit_event_outcome-list')
        self.url_detail = 'valuesets:audit_event_outcome-detail'
        self.model = AuditEventOutcome
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestAuditEventTypeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestAuditEventTypeViewSet, self).setUp()
        self.url_list = reverse('valuesets:audit_event_type-list')
        self.url_detail = 'valuesets:audit_event_type-detail'
        self.model = AuditEventType
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestBasicResourceTypeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestBasicResourceTypeViewSet, self).setUp()
        self.url_list = reverse('valuesets:basic_resource_type-list')
        self.url_detail = 'valuesets:basic_resource_type-detail'
        self.model = BasicResourceType
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestBenefitCategoryViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestBenefitCategoryViewSet, self).setUp()
        self.url_list = reverse('valuesets:benefit_category-list')
        self.url_detail = 'valuesets:benefit_category-detail'
        self.model = BenefitCategory
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestBenefitNetworkViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestBenefitNetworkViewSet, self).setUp()
        self.url_list = reverse('valuesets:benefit_network-list')
        self.url_detail = 'valuesets:benefit_network-detail'
        self.model = BenefitNetwork
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestBenefitSubcategoryViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestBenefitSubcategoryViewSet, self).setUp()
        self.url_list = reverse('valuesets:benefit_subcategory-list')
        self.url_detail = 'valuesets:benefit_subcategory-detail'
        self.model = BenefitSubcategory
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestBenefitTermViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestBenefitTermViewSet, self).setUp()
        self.url_list = reverse('valuesets:benefit_term-list')
        self.url_detail = 'valuesets:benefit_term-detail'
        self.model = BenefitTerm
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestBenefitTypeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestBenefitTypeViewSet, self).setUp()
        self.url_list = reverse('valuesets:benefit_type-list')
        self.url_detail = 'valuesets:benefit_type-detail'
        self.model = BenefitType
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestBenefitUnitViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestBenefitUnitViewSet, self).setUp()
        self.url_list = reverse('valuesets:benefit_unit-list')
        self.url_detail = 'valuesets:benefit_unit-detail'
        self.model = BenefitUnit
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestBindingStrengthViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestBindingStrengthViewSet, self).setUp()
        self.url_list = reverse('valuesets:binding_strength-list')
        self.url_detail = 'valuesets:binding_strength-detail'
        self.model = BindingStrength
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestBundleTypeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestBundleTypeViewSet, self).setUp()
        self.url_list = reverse('valuesets:bundle_type-list')
        self.url_detail = 'valuesets:bundle_type-detail'
        self.model = BundleType
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestCardinalityBehaviorViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestCardinalityBehaviorViewSet, self).setUp()
        self.url_list = reverse('valuesets:cardinality_behavior-list')
        self.url_detail = 'valuesets:cardinality_behavior-detail'
        self.model = CardinalityBehavior
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestCarePlanActivityCategoryViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestCarePlanActivityCategoryViewSet, self).setUp()
        self.url_list = reverse('valuesets:care_plan_activity_category-list')
        self.url_detail = 'valuesets:care_plan_activity_category-detail'
        self.model = CarePlanActivityCategory
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestCarePlanActivityStatusViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestCarePlanActivityStatusViewSet, self).setUp()
        self.url_list = reverse('valuesets:care_plan_activity_status-list')
        self.url_detail = 'valuesets:care_plan_activity_status-detail'
        self.model = CarePlanActivityStatus
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestCarePlanRelationshipViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestCarePlanRelationshipViewSet, self).setUp()
        self.url_list = reverse('valuesets:care_plan_relationship-list')
        self.url_detail = 'valuesets:care_plan_relationship-detail'
        self.model = CarePlanRelationship
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestCarePlanStatusViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestCarePlanStatusViewSet, self).setUp()
        self.url_list = reverse('valuesets:care_plan_status-list')
        self.url_detail = 'valuesets:care_plan_status-detail'
        self.model = CarePlanStatus
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestCdsRuleActionTypeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestCdsRuleActionTypeViewSet, self).setUp()
        self.url_list = reverse('valuesets:cds_rule_action_type-list')
        self.url_detail = 'valuesets:cds_rule_action_type-detail'
        self.model = CdsRuleActionType
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestCdsRuleParticipantViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestCdsRuleParticipantViewSet, self).setUp()
        self.url_list = reverse('valuesets:cds_rule_participant-list')
        self.url_detail = 'valuesets:cds_rule_participant-detail'
        self.model = CdsRuleParticipant
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestCdsRuleTriggerTypeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestCdsRuleTriggerTypeViewSet, self).setUp()
        self.url_list = reverse('valuesets:cds_rule_trigger_type-list')
        self.url_detail = 'valuesets:cds_rule_trigger_type-detail'
        self.model = CdsRuleTriggerType
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestChoiceListOrientationViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestChoiceListOrientationViewSet, self).setUp()
        self.url_list = reverse('valuesets:choice_list_orientation-list')
        self.url_detail = 'valuesets:choice_list_orientation-detail'
        self.model = ChoiceListOrientation
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestChromosomeHumanViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestChromosomeHumanViewSet, self).setUp()
        self.url_list = reverse('valuesets:chromosome_human-list')
        self.url_detail = 'valuesets:chromosome_human-detail'
        self.model = ChromosomeHuman
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestClaimExceptionViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestClaimExceptionViewSet, self).setUp()
        self.url_list = reverse('valuesets:claim_exception-list')
        self.url_detail = 'valuesets:claim_exception-detail'
        self.model = ClaimException
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestClaimTypeLinkViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestClaimTypeLinkViewSet, self).setUp()
        self.url_list = reverse('valuesets:claim_type_link-list')
        self.url_detail = 'valuesets:claim_type_link-detail'
        self.model = ClaimTypeLink
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestClaimTypeLink2ViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestClaimTypeLink2ViewSet, self).setUp()
        self.url_list = reverse('valuesets:claim_type_link2-list')
        self.url_detail = 'valuesets:claim_type_link2-detail'
        self.model = ClaimTypeLink2
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestClaimUseLinkViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestClaimUseLinkViewSet, self).setUp()
        self.url_list = reverse('valuesets:claim_use_link-list')
        self.url_detail = 'valuesets:claim_use_link-detail'
        self.model = ClaimUseLink
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestClaimCareteamroleViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestClaimCareteamroleViewSet, self).setUp()
        self.url_list = reverse('valuesets:claim_careteamrole-list')
        self.url_detail = 'valuesets:claim_careteamrole-detail'
        self.model = ClaimCareteamrole
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestClaimInformationcategoryViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestClaimInformationcategoryViewSet, self).setUp()
        self.url_list = reverse('valuesets:claim_informationcategory-list')
        self.url_detail = 'valuesets:claim_informationcategory-detail'
        self.model = ClaimInformationcategory
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestClassificationOrContextViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestClassificationOrContextViewSet, self).setUp()
        self.url_list = reverse('valuesets:classification_or_context-list')
        self.url_detail = 'valuesets:classification_or_context-detail'
        self.model = ClassificationOrContext
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestClinicalImpressionStatusViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestClinicalImpressionStatusViewSet, self).setUp()
        self.url_list = reverse('valuesets:clinical_impression_status-list')
        self.url_detail = 'valuesets:clinical_impression_status-detail'
        self.model = ClinicalImpressionStatus
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestContentModeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestContentModeViewSet, self).setUp()
        self.url_list = reverse('valuesets:content_mode-list')
        self.url_detail = 'valuesets:content_mode-detail'
        self.model = ContentMode
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestCommunicationRequestStatusViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestCommunicationRequestStatusViewSet, self).setUp()
        self.url_list = reverse('valuesets:communication_request_status-list')
        self.url_detail = 'valuesets:communication_request_status-detail'
        self.model = CommunicationRequestStatus
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestCommunicationStatusViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestCommunicationStatusViewSet, self).setUp()
        self.url_list = reverse('valuesets:communication_status-list')
        self.url_detail = 'valuesets:communication_status-detail'
        self.model = CommunicationStatus
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestCompartmentTypeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestCompartmentTypeViewSet, self).setUp()
        self.url_list = reverse('valuesets:compartment_type-list')
        self.url_detail = 'valuesets:compartment_type-detail'
        self.model = CompartmentType
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestCompositionAttestationModeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestCompositionAttestationModeViewSet, self).setUp()
        self.url_list = reverse('valuesets:composition_attestation_mode-list')
        self.url_detail = 'valuesets:composition_attestation_mode-detail'
        self.model = CompositionAttestationMode
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestCompositionStatusViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestCompositionStatusViewSet, self).setUp()
        self.url_list = reverse('valuesets:composition_status-list')
        self.url_detail = 'valuesets:composition_status-detail'
        self.model = CompositionStatus
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestConceptMapEquivalenceViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestConceptMapEquivalenceViewSet, self).setUp()
        self.url_list = reverse('valuesets:concept_map_equivalence-list')
        self.url_detail = 'valuesets:concept_map_equivalence-detail'
        self.model = ConceptMapEquivalence
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestConceptPropertiesViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestConceptPropertiesViewSet, self).setUp()
        self.url_list = reverse('valuesets:concept_properties-list')
        self.url_detail = 'valuesets:concept_properties-detail'
        self.model = ConceptProperties
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestConceptPropertyTypeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestConceptPropertyTypeViewSet, self).setUp()
        self.url_list = reverse('valuesets:concept_property_type-list')
        self.url_detail = 'valuesets:concept_property_type-detail'
        self.model = ConceptPropertyType
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestConditionCategoryViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestConditionCategoryViewSet, self).setUp()
        self.url_list = reverse('valuesets:condition_category-list')
        self.url_detail = 'valuesets:condition_category-detail'
        self.model = ConditionCategory
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestConditionClinicalViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestConditionClinicalViewSet, self).setUp()
        self.url_list = reverse('valuesets:condition_clinical-list')
        self.url_detail = 'valuesets:condition_clinical-detail'
        self.model = ConditionClinical
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestConditionStateViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestConditionStateViewSet, self).setUp()
        self.url_list = reverse('valuesets:condition_state-list')
        self.url_detail = 'valuesets:condition_state-detail'
        self.model = ConditionState
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestConditionVerStatusViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestConditionVerStatusViewSet, self).setUp()
        self.url_list = reverse('valuesets:condition_ver_status-list')
        self.url_detail = 'valuesets:condition_ver_status-detail'
        self.model = ConditionVerStatus
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestConditionalDeleteStatusViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestConditionalDeleteStatusViewSet, self).setUp()
        self.url_list = reverse('valuesets:conditional_delete_status-list')
        self.url_detail = 'valuesets:conditional_delete_status-detail'
        self.model = ConditionalDeleteStatus
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestConformanceExpectationViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestConformanceExpectationViewSet, self).setUp()
        self.url_list = reverse('valuesets:conformance_expectation-list')
        self.url_detail = 'valuesets:conformance_expectation-detail'
        self.model = ConformanceExpectation
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestConformanceResourceStatusViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestConformanceResourceStatusViewSet, self).setUp()
        self.url_list = reverse('valuesets:conformance_resource_status-list')
        self.url_detail = 'valuesets:conformance_resource_status-detail'
        self.model = ConformanceResourceStatus
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestConformanceStatementKindViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestConformanceStatementKindViewSet, self).setUp()
        self.url_list = reverse('valuesets:conformance_statement_kind-list')
        self.url_detail = 'valuesets:conformance_statement_kind-detail'
        self.model = ConformanceStatementKind
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestConsentDataMeaningViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestConsentDataMeaningViewSet, self).setUp()
        self.url_list = reverse('valuesets:consent_data_meaning-list')
        self.url_detail = 'valuesets:consent_data_meaning-detail'
        self.model = ConsentDataMeaning
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestConsentExceptTypeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestConsentExceptTypeViewSet, self).setUp()
        self.url_list = reverse('valuesets:consent_except_type-list')
        self.url_detail = 'valuesets:consent_except_type-detail'
        self.model = ConsentExceptType
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestConsentStatusViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestConsentStatusViewSet, self).setUp()
        self.url_list = reverse('valuesets:consent_status-list')
        self.url_detail = 'valuesets:consent_status-detail'
        self.model = ConsentStatus
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestConsentActionViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestConsentActionViewSet, self).setUp()
        self.url_list = reverse('valuesets:consent_action-list')
        self.url_detail = 'valuesets:consent_action-detail'
        self.model = ConsentAction
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestConsentCategoryViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestConsentCategoryViewSet, self).setUp()
        self.url_list = reverse('valuesets:consent_category-list')
        self.url_detail = 'valuesets:consent_category-detail'
        self.model = ConsentCategory
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestConstraintSeverityViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestConstraintSeverityViewSet, self).setUp()
        self.url_list = reverse('valuesets:constraint_severity-list')
        self.url_detail = 'valuesets:constraint_severity-detail'
        self.model = ConstraintSeverity
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestContactPointSystemViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestContactPointSystemViewSet, self).setUp()
        self.url_list = reverse('valuesets:contact_point_system-list')
        self.url_detail = 'valuesets:contact_point_system-detail'
        self.model = ContactPointSystem
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestContactPointUseViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestContactPointUseViewSet, self).setUp()
        self.url_list = reverse('valuesets:contact_point_use-list')
        self.url_detail = 'valuesets:contact_point_use-detail'
        self.model = ContactPointUse
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestContactentityTypeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestContactentityTypeViewSet, self).setUp()
        self.url_list = reverse('valuesets:contactentity_type-list')
        self.url_detail = 'valuesets:contactentity_type-detail'
        self.model = ContactentityType
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestContentTypeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestContentTypeViewSet, self).setUp()
        self.url_list = reverse('valuesets:content_type-list')
        self.url_detail = 'valuesets:content_type-detail'
        self.model = ContentType
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestContractSubtypeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestContractSubtypeViewSet, self).setUp()
        self.url_list = reverse('valuesets:contract_subtype-list')
        self.url_detail = 'valuesets:contract_subtype-detail'
        self.model = ContractSubtype
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestContractTermSubtypeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestContractTermSubtypeViewSet, self).setUp()
        self.url_list = reverse('valuesets:contract_term_subtype-list')
        self.url_detail = 'valuesets:contract_term_subtype-detail'
        self.model = ContractTermSubtype
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestContractTermTypeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestContractTermTypeViewSet, self).setUp()
        self.url_list = reverse('valuesets:contract_term_type-list')
        self.url_detail = 'valuesets:contract_term_type-detail'
        self.model = ContractTermType
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestContractTypeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestContractTypeViewSet, self).setUp()
        self.url_list = reverse('valuesets:contract_type-list')
        self.url_detail = 'valuesets:contract_type-detail'
        self.model = ContractType
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestCopyNumberEventViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestCopyNumberEventViewSet, self).setUp()
        self.url_list = reverse('valuesets:copy_number_event-list')
        self.url_detail = 'valuesets:copy_number_event-detail'
        self.model = CopyNumberEvent
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestCoverageExceptionViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestCoverageExceptionViewSet, self).setUp()
        self.url_list = reverse('valuesets:coverage_exception-list')
        self.url_detail = 'valuesets:coverage_exception-detail'
        self.model = CoverageException
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestDwebtypeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestDwebtypeViewSet, self).setUp()
        self.url_list = reverse('valuesets:dWebType-list')
        self.url_detail = 'valuesets:dWebType-detail'
        self.model = Dwebtype
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestDataAbsentReasonViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestDataAbsentReasonViewSet, self).setUp()
        self.url_list = reverse('valuesets:data_absent_reason-list')
        self.url_detail = 'valuesets:data_absent_reason-detail'
        self.model = DataAbsentReason
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestDataTypesViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestDataTypesViewSet, self).setUp()
        self.url_list = reverse('valuesets:data_types-list')
        self.url_detail = 'valuesets:data_types-detail'
        self.model = DataTypes
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestDataelementStringencyViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestDataelementStringencyViewSet, self).setUp()
        self.url_list = reverse('valuesets:dataelement_stringency-list')
        self.url_detail = 'valuesets:dataelement_stringency-detail'
        self.model = DataelementStringency
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestDaysOfWeekViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestDaysOfWeekViewSet, self).setUp()
        self.url_list = reverse('valuesets:days_of_week-list')
        self.url_detail = 'valuesets:days_of_week-detail'
        self.model = DaysOfWeek
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestDetectedissueSeverityViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestDetectedissueSeverityViewSet, self).setUp()
        self.url_list = reverse('valuesets:detectedissue_severity-list')
        self.url_detail = 'valuesets:detectedissue_severity-detail'
        self.model = DetectedissueSeverity
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestDeviceActionViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestDeviceActionViewSet, self).setUp()
        self.url_list = reverse('valuesets:device_action-list')
        self.url_detail = 'valuesets:device_action-detail'
        self.model = DeviceAction
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestDeviceUseRequestPriorityViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestDeviceUseRequestPriorityViewSet, self).setUp()
        self.url_list = reverse('valuesets:device_use_request_priority-list')
        self.url_detail = 'valuesets:device_use_request_priority-detail'
        self.model = DeviceUseRequestPriority
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestDeviceUseRequestStatusViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestDeviceUseRequestStatusViewSet, self).setUp()
        self.url_list = reverse('valuesets:device_use_request_status-list')
        self.url_detail = 'valuesets:device_use_request_status-detail'
        self.model = DeviceUseRequestStatus
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestDevicestatusViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestDevicestatusViewSet, self).setUp()
        self.url_list = reverse('valuesets:devicestatus-list')
        self.url_detail = 'valuesets:devicestatus-detail'
        self.model = Devicestatus
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestDiagnosticOrderPriorityViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestDiagnosticOrderPriorityViewSet, self).setUp()
        self.url_list = reverse('valuesets:diagnostic_order_priority-list')
        self.url_detail = 'valuesets:diagnostic_order_priority-detail'
        self.model = DiagnosticOrderPriority
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestDiagnosticOrderStatusViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestDiagnosticOrderStatusViewSet, self).setUp()
        self.url_list = reverse('valuesets:diagnostic_order_status-list')
        self.url_detail = 'valuesets:diagnostic_order_status-detail'
        self.model = DiagnosticOrderStatus
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestDiagnosticReportStatusViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestDiagnosticReportStatusViewSet, self).setUp()
        self.url_list = reverse('valuesets:diagnostic_report_status-list')
        self.url_detail = 'valuesets:diagnostic_report_status-detail'
        self.model = DiagnosticReportStatus
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestEncounterDietViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestEncounterDietViewSet, self).setUp()
        self.url_list = reverse('valuesets:encounter_diet-list')
        self.url_detail = 'valuesets:encounter_diet-detail'
        self.model = EncounterDiet
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestDigitalMediaTypeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestDigitalMediaTypeViewSet, self).setUp()
        self.url_list = reverse('valuesets:digital_media_type-list')
        self.url_detail = 'valuesets:digital_media_type-detail'
        self.model = DigitalMediaType
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestEncounterDischargeDispositionViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestEncounterDischargeDispositionViewSet, self).setUp()
        self.url_list = reverse(
            'valuesets:encounter_discharge_disposition-list')
        self.url_detail = 'valuesets:encounter_discharge_disposition-detail'
        self.model = EncounterDischargeDisposition
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestDocumentModeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestDocumentModeViewSet, self).setUp()
        self.url_list = reverse('valuesets:document_mode-list')
        self.url_detail = 'valuesets:document_mode-detail'
        self.model = DocumentMode
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestDocumentReferenceStatusViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestDocumentReferenceStatusViewSet, self).setUp()
        self.url_list = reverse('valuesets:document_reference_status-list')
        self.url_detail = 'valuesets:document_reference_status-detail'
        self.model = DocumentReferenceStatus
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestDocumentRelationshipTypeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestDocumentRelationshipTypeViewSet, self).setUp()
        self.url_list = reverse('valuesets:document_relationship_type-list')
        self.url_detail = 'valuesets:document_relationship_type-detail'
        self.model = DocumentRelationshipType
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestEncounterLocationStatusViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestEncounterLocationStatusViewSet, self).setUp()
        self.url_list = reverse('valuesets:encounter_location_status-list')
        self.url_detail = 'valuesets:encounter_location_status-detail'
        self.model = EncounterLocationStatus
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestEncounterPriorityViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestEncounterPriorityViewSet, self).setUp()
        self.url_list = reverse('valuesets:encounter_priority-list')
        self.url_detail = 'valuesets:encounter_priority-detail'
        self.model = EncounterPriority
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestEncounterSpecialArrangementsViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestEncounterSpecialArrangementsViewSet, self).setUp()
        self.url_list = reverse('valuesets:encounter_special_arrangements-list')
        self.url_detail = 'valuesets:encounter_special_arrangements-detail'
        self.model = EncounterSpecialArrangements
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestEncounterStateViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestEncounterStateViewSet, self).setUp()
        self.url_list = reverse('valuesets:encounter_state-list')
        self.url_detail = 'valuesets:encounter_state-detail'
        self.model = EncounterState
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestEncounterTypeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestEncounterTypeViewSet, self).setUp()
        self.url_list = reverse('valuesets:encounter_type-list')
        self.url_detail = 'valuesets:encounter_type-detail'
        self.model = EncounterType
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestEndpointStatusViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestEndpointStatusViewSet, self).setUp()
        self.url_list = reverse('valuesets:endpoint_status-list')
        self.url_detail = 'valuesets:endpoint_status-detail'
        self.model = EndpointStatus
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestEntformulaAdditiveViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestEntformulaAdditiveViewSet, self).setUp()
        self.url_list = reverse('valuesets:entformula_additive-list')
        self.url_detail = 'valuesets:entformula_additive-detail'
        self.model = EntformulaAdditive
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestEpisodeOfCareStatusViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestEpisodeOfCareStatusViewSet, self).setUp()
        self.url_list = reverse('valuesets:episode_of_care_status-list')
        self.url_detail = 'valuesets:episode_of_care_status-detail'
        self.model = EpisodeOfCareStatus
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestServiceUsclsViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestServiceUsclsViewSet, self).setUp()
        self.url_list = reverse('valuesets:service_uscls-list')
        self.url_detail = 'valuesets:service_uscls-detail'
        self.model = ServiceUscls
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestFmItemtypeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestFmItemtypeViewSet, self).setUp()
        self.url_list = reverse('valuesets:fm_itemtype-list')
        self.url_detail = 'valuesets:fm_itemtype-detail'
        self.model = FmItemtype
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestOccurrenceCodesViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestOccurrenceCodesViewSet, self).setUp()
        self.url_list = reverse('valuesets:occurrence_codes-list')
        self.url_detail = 'valuesets:occurrence_codes-detail'
        self.model = OccurrenceCodes
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestOccurrenceSpanCodesViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestOccurrenceSpanCodesViewSet, self).setUp()
        self.url_list = reverse('valuesets:occurrence_span_codes-list')
        self.url_detail = 'valuesets:occurrence_span_codes-detail'
        self.model = OccurrenceSpanCodes
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestClaimSubtypeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestClaimSubtypeViewSet, self).setUp()
        self.url_list = reverse('valuesets:claim_subtype-list')
        self.url_detail = 'valuesets:claim_subtype-detail'
        self.model = ClaimSubtype
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestValueCodesViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestValueCodesViewSet, self).setUp()
        self.url_list = reverse('valuesets:value_codes-list')
        self.url_detail = 'valuesets:value_codes-detail'
        self.model = ValueCodes
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestExDiagnosisrelatedgroupViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestExDiagnosisrelatedgroupViewSet, self).setUp()
        self.url_list = reverse('valuesets:ex_diagnosisrelatedgroup-list')
        self.url_detail = 'valuesets:ex_diagnosisrelatedgroup-detail'
        self.model = ExDiagnosisrelatedgroup
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestExDiagnosistypeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestExDiagnosistypeViewSet, self).setUp()
        self.url_list = reverse('valuesets:ex_diagnosistype-list')
        self.url_detail = 'valuesets:ex_diagnosistype-detail'
        self.model = ExDiagnosistype
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestTeethViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestTeethViewSet, self).setUp()
        self.url_list = reverse('valuesets:teeth-list')
        self.url_detail = 'valuesets:teeth-detail'
        self.model = Teeth
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestExOnsettypeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestExOnsettypeViewSet, self).setUp()
        self.url_list = reverse('valuesets:ex_onsettype-list')
        self.url_detail = 'valuesets:ex_onsettype-detail'
        self.model = ExOnsettype
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestOralProsthodonticMaterialViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestOralProsthodonticMaterialViewSet, self).setUp()
        self.url_list = reverse('valuesets:oral_prosthodontic_material-list')
        self.url_detail = 'valuesets:oral_prosthodontic_material-detail'
        self.model = OralProsthodonticMaterial
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestExPaymenttypeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestExPaymenttypeViewSet, self).setUp()
        self.url_list = reverse('valuesets:ex_paymenttype-list')
        self.url_detail = 'valuesets:ex_paymenttype-detail'
        self.model = ExPaymenttype
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestServicePharmacyViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestServicePharmacyViewSet, self).setUp()
        self.url_list = reverse('valuesets:service_pharmacy-list')
        self.url_detail = 'valuesets:service_pharmacy-detail'
        self.model = ServicePharmacy
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestExProgramCodeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestExProgramCodeViewSet, self).setUp()
        self.url_list = reverse('valuesets:ex_program_code-list')
        self.url_detail = 'valuesets:ex_program_code-detail'
        self.model = ExProgramCode
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestProviderQualificationViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestProviderQualificationViewSet, self).setUp()
        self.url_list = reverse('valuesets:provider_qualification-list')
        self.url_detail = 'valuesets:provider_qualification-detail'
        self.model = ProviderQualification
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestRelatedClaimRelationshipViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestRelatedClaimRelationshipViewSet, self).setUp()
        self.url_list = reverse('valuesets:related_claim_relationship-list')
        self.url_detail = 'valuesets:related_claim_relationship-detail'
        self.model = RelatedClaimRelationship
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestServiceModifiersViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestServiceModifiersViewSet, self).setUp()
        self.url_list = reverse('valuesets:service_modifiers-list')
        self.url_detail = 'valuesets:service_modifiers-detail'
        self.model = ServiceModifiers
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestServicePlaceViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestServicePlaceViewSet, self).setUp()
        self.url_list = reverse('valuesets:service_place-list')
        self.url_detail = 'valuesets:service_place-detail'
        self.model = ServicePlace
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestServiceProductViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestServiceProductViewSet, self).setUp()
        self.url_list = reverse('valuesets:service_product-list')
        self.url_detail = 'valuesets:service_product-detail'
        self.model = ServiceProduct
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestToothViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestToothViewSet, self).setUp()
        self.url_list = reverse('valuesets:tooth-list')
        self.url_detail = 'valuesets:tooth-detail'
        self.model = Tooth
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestUdiViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestUdiViewSet, self).setUp()
        self.url_list = reverse('valuesets:udi-list')
        self.url_detail = 'valuesets:udi-detail'
        self.model = Udi
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestVisionProductViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestVisionProductViewSet, self).setUp()
        self.url_list = reverse('valuesets:vision_product-list')
        self.url_detail = 'valuesets:vision_product-detail'
        self.model = VisionProduct
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestExtensionContextViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestExtensionContextViewSet, self).setUp()
        self.url_list = reverse('valuesets:extension_context-list')
        self.url_detail = 'valuesets:extension_context-detail'
        self.model = ExtensionContext
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestFilterOperatorViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestFilterOperatorViewSet, self).setUp()
        self.url_list = reverse('valuesets:filter_operator-list')
        self.url_detail = 'valuesets:filter_operator-detail'
        self.model = FilterOperator
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestFlagCategoryViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestFlagCategoryViewSet, self).setUp()
        self.url_list = reverse('valuesets:flag_category-list')
        self.url_detail = 'valuesets:flag_category-detail'
        self.model = FlagCategory
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestFlagPriorityViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestFlagPriorityViewSet, self).setUp()
        self.url_list = reverse('valuesets:flag_priority-list')
        self.url_detail = 'valuesets:flag_priority-detail'
        self.model = FlagPriority
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestFlagStatusViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestFlagStatusViewSet, self).setUp()
        self.url_list = reverse('valuesets:flag_status-list')
        self.url_detail = 'valuesets:flag_status-detail'
        self.model = FlagStatus
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestFmConditionsViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestFmConditionsViewSet, self).setUp()
        self.url_list = reverse('valuesets:fm_conditions-list')
        self.url_detail = 'valuesets:fm_conditions-detail'
        self.model = FmConditions
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestFormsViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestFormsViewSet, self).setUp()
        self.url_list = reverse('valuesets:forms-list')
        self.url_detail = 'valuesets:forms-detail'
        self.model = Forms
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestFundsreserveViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestFundsreserveViewSet, self).setUp()
        self.url_list = reverse('valuesets:fundsreserve-list')
        self.url_detail = 'valuesets:fundsreserve-detail'
        self.model = Fundsreserve
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestGoalAcceptanceStatusViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestGoalAcceptanceStatusViewSet, self).setUp()
        self.url_list = reverse('valuesets:goal_acceptance_status-list')
        self.url_detail = 'valuesets:goal_acceptance_status-detail'
        self.model = GoalAcceptanceStatus
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestGoalCategoryViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestGoalCategoryViewSet, self).setUp()
        self.url_list = reverse('valuesets:goal_category-list')
        self.url_detail = 'valuesets:goal_category-detail'
        self.model = GoalCategory
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestGoalPriorityViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestGoalPriorityViewSet, self).setUp()
        self.url_list = reverse('valuesets:goal_priority-list')
        self.url_detail = 'valuesets:goal_priority-detail'
        self.model = GoalPriority
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestGoalRelationshipTypeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestGoalRelationshipTypeViewSet, self).setUp()
        self.url_list = reverse('valuesets:goal_relationship_type-list')
        self.url_detail = 'valuesets:goal_relationship_type-detail'
        self.model = GoalRelationshipType
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestGoalStatusViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestGoalStatusViewSet, self).setUp()
        self.url_list = reverse('valuesets:goal_status-list')
        self.url_detail = 'valuesets:goal_status-detail'
        self.model = GoalStatus
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestGoalStatusReasonViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestGoalStatusReasonViewSet, self).setUp()
        self.url_list = reverse('valuesets:goal_status_reason-list')
        self.url_detail = 'valuesets:goal_status_reason-detail'
        self.model = GoalStatusReason
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestGroupTypeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestGroupTypeViewSet, self).setUp()
        self.url_list = reverse('valuesets:group_type-list')
        self.url_detail = 'valuesets:group_type-detail'
        self.model = GroupType
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestGroupingBehaviorViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestGroupingBehaviorViewSet, self).setUp()
        self.url_list = reverse('valuesets:grouping_behavior-list')
        self.url_detail = 'valuesets:grouping_behavior-detail'
        self.model = GroupingBehavior
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestGuidanceResponseStatusViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestGuidanceResponseStatusViewSet, self).setUp()
        self.url_list = reverse('valuesets:guidance_response_status-list')
        self.url_detail = 'valuesets:guidance_response_status-detail'
        self.model = GuidanceResponseStatus
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestGuideDependencyTypeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestGuideDependencyTypeViewSet, self).setUp()
        self.url_list = reverse('valuesets:guide_dependency_type-list')
        self.url_detail = 'valuesets:guide_dependency_type-detail'
        self.model = GuideDependencyType
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestGuidePageKindViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestGuidePageKindViewSet, self).setUp()
        self.url_list = reverse('valuesets:guide_page_kind-list')
        self.url_detail = 'valuesets:guide_page_kind-detail'
        self.model = GuidePageKind
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestHistoryStatusViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestHistoryStatusViewSet, self).setUp()
        self.url_list = reverse('valuesets:history_status-list')
        self.url_detail = 'valuesets:history_status-detail'
        self.model = HistoryStatus
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestHttpVerbViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestHttpVerbViewSet, self).setUp()
        self.url_list = reverse('valuesets:http_verb-list')
        self.url_detail = 'valuesets:http_verb-detail'
        self.model = HttpVerb
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestIdentifierTypeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestIdentifierTypeViewSet, self).setUp()
        self.url_list = reverse('valuesets:identifier_type-list')
        self.url_detail = 'valuesets:identifier_type-detail'
        self.model = IdentifierType
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestIdentifierUseViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestIdentifierUseViewSet, self).setUp()
        self.url_list = reverse('valuesets:identifier_use-list')
        self.url_detail = 'valuesets:identifier_use-detail'
        self.model = IdentifierUse
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestIdentityAssurancelevelViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestIdentityAssurancelevelViewSet, self).setUp()
        self.url_list = reverse('valuesets:identity_assuranceLevel-list')
        self.url_detail = 'valuesets:identity_assuranceLevel-detail'
        self.model = IdentityAssurancelevel
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestImmunizationRecommendationDateCriterionViewSet(
        APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestImmunizationRecommendationDateCriterionViewSet, self).setUp()
        self.url_list = reverse(
            'valuesets:immunization_recommendation_date_criterion-list')
        self.url_detail = (
            'valuesets:immunization_recommendation_date_criterion-detail')
        self.model = ImmunizationRecommendationDateCriterion
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestImmunizationRecommendationStatusViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestImmunizationRecommendationStatusViewSet, self).setUp()
        self.url_list = reverse(
            'valuesets:immunization_recommendation_status-list')
        self.url_detail = 'valuesets:immunization_recommendation_status-detail'
        self.model = ImmunizationRecommendationStatus
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestInterventionViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestInterventionViewSet, self).setUp()
        self.url_list = reverse('valuesets:intervention-list')
        self.url_detail = 'valuesets:intervention-detail'
        self.model = Intervention
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestIssueSeverityViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestIssueSeverityViewSet, self).setUp()
        self.url_list = reverse('valuesets:issue_severity-list')
        self.url_detail = 'valuesets:issue_severity-detail'
        self.model = IssueSeverity
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestIssueTypeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestIssueTypeViewSet, self).setUp()
        self.url_list = reverse('valuesets:issue_type-list')
        self.url_detail = 'valuesets:issue_type-detail'
        self.model = IssueType
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestItemTypeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestItemTypeViewSet, self).setUp()
        self.url_list = reverse('valuesets:item_type-list')
        self.url_detail = 'valuesets:item_type-detail'
        self.model = ItemType
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestLinkTypeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestLinkTypeViewSet, self).setUp()
        self.url_list = reverse('valuesets:link_type-list')
        self.url_detail = 'valuesets:link_type-detail'
        self.model = LinkType
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestLinkageTypeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestLinkageTypeViewSet, self).setUp()
        self.url_list = reverse('valuesets:linkage_type-list')
        self.url_detail = 'valuesets:linkage_type-detail'
        self.model = LinkageType
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestListEmptyReasonViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestListEmptyReasonViewSet, self).setUp()
        self.url_list = reverse('valuesets:list_empty_reason-list')
        self.url_detail = 'valuesets:list_empty_reason-detail'
        self.model = ListEmptyReason
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestListExampleCodesViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestListExampleCodesViewSet, self).setUp()
        self.url_list = reverse('valuesets:list_example_codes-list')
        self.url_detail = 'valuesets:list_example_codes-detail'
        self.model = ListExampleCodes
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestListModeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestListModeViewSet, self).setUp()
        self.url_list = reverse('valuesets:list_mode-list')
        self.url_detail = 'valuesets:list_mode-detail'
        self.model = ListMode
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestListOrderViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestListOrderViewSet, self).setUp()
        self.url_list = reverse('valuesets:list_order-list')
        self.url_detail = 'valuesets:list_order-detail'
        self.model = ListOrder
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestListStatusViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestListStatusViewSet, self).setUp()
        self.url_list = reverse('valuesets:list_status-list')
        self.url_detail = 'valuesets:list_status-detail'
        self.model = ListStatus
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestLocationModeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestLocationModeViewSet, self).setUp()
        self.url_list = reverse('valuesets:location_mode-list')
        self.url_detail = 'valuesets:location_mode-detail'
        self.model = LocationMode
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestLocationPhysicalTypeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestLocationPhysicalTypeViewSet, self).setUp()
        self.url_list = reverse('valuesets:location_physical_type-list')
        self.url_detail = 'valuesets:location_physical_type-detail'
        self.model = LocationPhysicalType
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestLocationStatusViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestLocationStatusViewSet, self).setUp()
        self.url_list = reverse('valuesets:location_status-list')
        self.url_detail = 'valuesets:location_status-detail'
        self.model = LocationStatus
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestMapContextTypeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestMapContextTypeViewSet, self).setUp()
        self.url_list = reverse('valuesets:map_context_type-list')
        self.url_detail = 'valuesets:map_context_type-detail'
        self.model = MapContextType
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestMapInputModeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestMapInputModeViewSet, self).setUp()
        self.url_list = reverse('valuesets:map_input_mode-list')
        self.url_detail = 'valuesets:map_input_mode-detail'
        self.model = MapInputMode
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestMapListModeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestMapListModeViewSet, self).setUp()
        self.url_list = reverse('valuesets:map_list_mode-list')
        self.url_detail = 'valuesets:map_list_mode-detail'
        self.model = MapListMode
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestMapModelModeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestMapModelModeViewSet, self).setUp()
        self.url_list = reverse('valuesets:map_model_mode-list')
        self.url_detail = 'valuesets:map_model_mode-detail'
        self.model = MapModelMode
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestMapTransformViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestMapTransformViewSet, self).setUp()
        self.url_list = reverse('valuesets:map_transform-list')
        self.url_detail = 'valuesets:map_transform-detail'
        self.model = MapTransform
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestMaritalStatusViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestMaritalStatusViewSet, self).setUp()
        self.url_list = reverse('valuesets:marital_status-list')
        self.url_detail = 'valuesets:marital_status-detail'
        self.model = MaritalStatus
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestMatchGradeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestMatchGradeViewSet, self).setUp()
        self.url_list = reverse('valuesets:match_grade-list')
        self.url_detail = 'valuesets:match_grade-detail'
        self.model = MatchGrade
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestMeasureDataUsageViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestMeasureDataUsageViewSet, self).setUp()
        self.url_list = reverse('valuesets:measure_data_usage-list')
        self.url_detail = 'valuesets:measure_data_usage-detail'
        self.model = MeasureDataUsage
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestMeasurePopulationViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestMeasurePopulationViewSet, self).setUp()
        self.url_list = reverse('valuesets:measure_population-list')
        self.url_detail = 'valuesets:measure_population-detail'
        self.model = MeasurePopulation
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestMeasureReportStatusViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestMeasureReportStatusViewSet, self).setUp()
        self.url_list = reverse('valuesets:measure_report_status-list')
        self.url_detail = 'valuesets:measure_report_status-detail'
        self.model = MeasureReportStatus
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestMeasureReportTypeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestMeasureReportTypeViewSet, self).setUp()
        self.url_list = reverse('valuesets:measure_report_type-list')
        self.url_detail = 'valuesets:measure_report_type-detail'
        self.model = MeasureReportType
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestMeasureScoringViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestMeasureScoringViewSet, self).setUp()
        self.url_list = reverse('valuesets:measure_scoring-list')
        self.url_detail = 'valuesets:measure_scoring-detail'
        self.model = MeasureScoring
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestMeasureTypeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestMeasureTypeViewSet, self).setUp()
        self.url_list = reverse('valuesets:measure_type-list')
        self.url_detail = 'valuesets:measure_type-detail'
        self.model = MeasureType
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestMeasurementPrincipleViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestMeasurementPrincipleViewSet, self).setUp()
        self.url_list = reverse('valuesets:measurement_principle-list')
        self.url_detail = 'valuesets:measurement_principle-detail'
        self.model = MeasurementPrinciple
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestDigitalMediaSubtypeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestDigitalMediaSubtypeViewSet, self).setUp()
        self.url_list = reverse('valuesets:digital_media_subtype-list')
        self.url_detail = 'valuesets:digital_media_subtype-detail'
        self.model = DigitalMediaSubtype
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestMedicationAdminStatusViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestMedicationAdminStatusViewSet, self).setUp()
        self.url_list = reverse('valuesets:medication_admin_status-list')
        self.url_detail = 'valuesets:medication_admin_status-detail'
        self.model = MedicationAdminStatus
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestMedicationDispenseStatusViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestMedicationDispenseStatusViewSet, self).setUp()
        self.url_list = reverse('valuesets:medication_dispense_status-list')
        self.url_detail = 'valuesets:medication_dispense_status-detail'
        self.model = MedicationDispenseStatus
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestMedicationOrderStatusViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestMedicationOrderStatusViewSet, self).setUp()
        self.url_list = reverse('valuesets:medication_order_status-list')
        self.url_detail = 'valuesets:medication_order_status-detail'
        self.model = MedicationOrderStatus
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestMedicationStatementStatusViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestMedicationStatementStatusViewSet, self).setUp()
        self.url_list = reverse('valuesets:medication_statement_status-list')
        self.url_detail = 'valuesets:medication_statement_status-detail'
        self.model = MedicationStatementStatus
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestMessageConformanceEventModeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestMessageConformanceEventModeViewSet, self).setUp()
        self.url_list = reverse('valuesets:message_conformance_event_mode-list')
        self.url_detail = 'valuesets:message_conformance_event_mode-detail'
        self.model = MessageConformanceEventMode
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestMessageEventsViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestMessageEventsViewSet, self).setUp()
        self.url_list = reverse('valuesets:message_events-list')
        self.url_detail = 'valuesets:message_events-detail'
        self.model = MessageEvents
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestMessageReasonEncounterViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestMessageReasonEncounterViewSet, self).setUp()
        self.url_list = reverse('valuesets:message_reason_encounter-list')
        self.url_detail = 'valuesets:message_reason_encounter-detail'
        self.model = MessageReasonEncounter
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestMessageSignificanceCategoryViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestMessageSignificanceCategoryViewSet, self).setUp()
        self.url_list = reverse('valuesets:message_significance_category-list')
        self.url_detail = 'valuesets:message_significance_category-detail'
        self.model = MessageSignificanceCategory
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestMessageTransportViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestMessageTransportViewSet, self).setUp()
        self.url_list = reverse('valuesets:message_transport-list')
        self.url_detail = 'valuesets:message_transport-detail'
        self.model = MessageTransport
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestMetricCalibrationStateViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestMetricCalibrationStateViewSet, self).setUp()
        self.url_list = reverse('valuesets:metric_calibration_state-list')
        self.url_detail = 'valuesets:metric_calibration_state-detail'
        self.model = MetricCalibrationState
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestMetricCalibrationTypeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestMetricCalibrationTypeViewSet, self).setUp()
        self.url_list = reverse('valuesets:metric_calibration_type-list')
        self.url_detail = 'valuesets:metric_calibration_type-detail'
        self.model = MetricCalibrationType
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestMetricCategoryViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestMetricCategoryViewSet, self).setUp()
        self.url_list = reverse('valuesets:metric_category-list')
        self.url_detail = 'valuesets:metric_category-detail'
        self.model = MetricCategory
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestMetricColorViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestMetricColorViewSet, self).setUp()
        self.url_list = reverse('valuesets:metric_color-list')
        self.url_detail = 'valuesets:metric_color-detail'
        self.model = MetricColor
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestMetricOperationalStatusViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestMetricOperationalStatusViewSet, self).setUp()
        self.url_list = reverse('valuesets:metric_operational_status-list')
        self.url_detail = 'valuesets:metric_operational_status-detail'
        self.model = MetricOperationalStatus
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestMissingToothReasonViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestMissingToothReasonViewSet, self).setUp()
        self.url_list = reverse('valuesets:missing_tooth_reason-list')
        self.url_detail = 'valuesets:missing_tooth_reason-detail'
        self.model = MissingToothReason
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestClaimModifiersViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestClaimModifiersViewSet, self).setUp()
        self.url_list = reverse('valuesets:claim_modifiers-list')
        self.url_detail = 'valuesets:claim_modifiers-detail'
        self.model = ClaimModifiers
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestModuleMetadataContributorViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestModuleMetadataContributorViewSet, self).setUp()
        self.url_list = reverse('valuesets:module_metadata_contributor-list')
        self.url_detail = 'valuesets:module_metadata_contributor-detail'
        self.model = ModuleMetadataContributor
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestModuleMetadataFocusTypeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestModuleMetadataFocusTypeViewSet, self).setUp()
        self.url_list = reverse('valuesets:module_metadata_focus_type-list')
        self.url_detail = 'valuesets:module_metadata_focus_type-detail'
        self.model = ModuleMetadataFocusType
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestModuleMetadataResourceTypeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestModuleMetadataResourceTypeViewSet, self).setUp()
        self.url_list = reverse('valuesets:module_metadata_resource_type-list')
        self.url_detail = 'valuesets:module_metadata_resource_type-detail'
        self.model = ModuleMetadataResourceType
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestModuleMetadataStatusViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestModuleMetadataStatusViewSet, self).setUp()
        self.url_list = reverse('valuesets:module_metadata_status-list')
        self.url_detail = 'valuesets:module_metadata_status-detail'
        self.model = ModuleMetadataStatus
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestModuleMetadataTypeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestModuleMetadataTypeViewSet, self).setUp()
        self.url_list = reverse('valuesets:module_metadata_type-list')
        self.url_detail = 'valuesets:module_metadata_type-detail'
        self.model = ModuleMetadataType
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestNameUseViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestNameUseViewSet, self).setUp()
        self.url_list = reverse('valuesets:name_use-list')
        self.url_detail = 'valuesets:name_use-detail'
        self.model = NameUse
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestNamingsystemIdentifierTypeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestNamingsystemIdentifierTypeViewSet, self).setUp()
        self.url_list = reverse('valuesets:namingsystem_identifier_type-list')
        self.url_detail = 'valuesets:namingsystem_identifier_type-detail'
        self.model = NamingsystemIdentifierType
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestNamingsystemTypeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestNamingsystemTypeViewSet, self).setUp()
        self.url_list = reverse('valuesets:namingsystem_type-list')
        self.url_detail = 'valuesets:namingsystem_type-detail'
        self.model = NamingsystemType
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestNarrativeStatusViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestNarrativeStatusViewSet, self).setUp()
        self.url_list = reverse('valuesets:narrative_status-list')
        self.url_detail = 'valuesets:narrative_status-detail'
        self.model = NarrativeStatus
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestNetworkTypeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestNetworkTypeViewSet, self).setUp()
        self.url_list = reverse('valuesets:network_type-list')
        self.url_detail = 'valuesets:network_type-detail'
        self.model = NetworkType
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestNoteTypeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestNoteTypeViewSet, self).setUp()
        self.url_list = reverse('valuesets:note_type-list')
        self.url_detail = 'valuesets:note_type-detail'
        self.model = NoteType
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestNutritionOrderStatusViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestNutritionOrderStatusViewSet, self).setUp()
        self.url_list = reverse('valuesets:nutrition_order_status-list')
        self.url_detail = 'valuesets:nutrition_order_status-detail'
        self.model = NutritionOrderStatus
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestObjectLifecycleViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestObjectLifecycleViewSet, self).setUp()
        self.url_list = reverse('valuesets:object_lifecycle-list')
        self.url_detail = 'valuesets:object_lifecycle-detail'
        self.model = ObjectLifecycle
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestObjectRoleViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestObjectRoleViewSet, self).setUp()
        self.url_list = reverse('valuesets:object_role-list')
        self.url_detail = 'valuesets:object_role-detail'
        self.model = ObjectRole
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestObjectTypeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestObjectTypeViewSet, self).setUp()
        self.url_list = reverse('valuesets:object_type-list')
        self.url_detail = 'valuesets:object_type-detail'
        self.model = ObjectType
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestObservationCategoryViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestObservationCategoryViewSet, self).setUp()
        self.url_list = reverse('valuesets:observation_category-list')
        self.url_detail = 'valuesets:observation_category-detail'
        self.model = ObservationCategory
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestObservationParamcodeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestObservationParamcodeViewSet, self).setUp()
        self.url_list = reverse('valuesets:observation_paramcode-list')
        self.url_detail = 'valuesets:observation_paramcode-detail'
        self.model = ObservationParamcode
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestObservationRelationshiptypesViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestObservationRelationshiptypesViewSet, self).setUp()
        self.url_list = reverse('valuesets:observation_relationshiptypes-list')
        self.url_detail = 'valuesets:observation_relationshiptypes-detail'
        self.model = ObservationRelationshiptypes
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestObservationStatusViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestObservationStatusViewSet, self).setUp()
        self.url_list = reverse('valuesets:observation_status-list')
        self.url_detail = 'valuesets:observation_status-detail'
        self.model = ObservationStatus
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestOperationKindViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestOperationKindViewSet, self).setUp()
        self.url_list = reverse('valuesets:operation_kind-list')
        self.url_detail = 'valuesets:operation_kind-detail'
        self.model = OperationKind
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestOperationOutcomeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestOperationOutcomeViewSet, self).setUp()
        self.url_list = reverse('valuesets:operation_outcome-list')
        self.url_detail = 'valuesets:operation_outcome-detail'
        self.model = OperationOutcome
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestOperationParameterUseViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestOperationParameterUseViewSet, self).setUp()
        self.url_list = reverse('valuesets:operation_parameter_use-list')
        self.url_detail = 'valuesets:operation_parameter_use-detail'
        self.model = OperationParameterUse
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestOrderSetItemTypeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestOrderSetItemTypeViewSet, self).setUp()
        self.url_list = reverse('valuesets:order_set_item_type-list')
        self.url_detail = 'valuesets:order_set_item_type-detail'
        self.model = OrderSetItemType
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestOrderSetParticipantViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestOrderSetParticipantViewSet, self).setUp()
        self.url_list = reverse('valuesets:order_set_participant-list')
        self.url_detail = 'valuesets:order_set_participant-detail'
        self.model = OrderSetParticipant
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestOrderStatusViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestOrderStatusViewSet, self).setUp()
        self.url_list = reverse('valuesets:order_status-list')
        self.url_detail = 'valuesets:order_status-detail'
        self.model = OrderStatus
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestOrganizationTypeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestOrganizationTypeViewSet, self).setUp()
        self.url_list = reverse('valuesets:organization_type-list')
        self.url_detail = 'valuesets:organization_type-detail'
        self.model = OrganizationType
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestEncounterParticipantTypeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestEncounterParticipantTypeViewSet, self).setUp()
        self.url_list = reverse('valuesets:encounter_participant_type-list')
        self.url_detail = 'valuesets:encounter_participant_type-detail'
        self.model = EncounterParticipantType
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestParticipantrequiredViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestParticipantrequiredViewSet, self).setUp()
        self.url_list = reverse('valuesets:participantrequired-list')
        self.url_detail = 'valuesets:participantrequired-detail'
        self.model = Participantrequired
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestParticipationstatusViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestParticipationstatusViewSet, self).setUp()
        self.url_list = reverse('valuesets:participationstatus-list')
        self.url_detail = 'valuesets:participationstatus-detail'
        self.model = Participationstatus
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestPatientContactRelationshipViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestPatientContactRelationshipViewSet, self).setUp()
        self.url_list = reverse('valuesets:patient_contact_relationship-list')
        self.url_detail = 'valuesets:patient_contact_relationship-detail'
        self.model = PatientContactRelationship
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestPatientMpiMatchViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestPatientMpiMatchViewSet, self).setUp()
        self.url_list = reverse('valuesets:patient_mpi_match-list')
        self.url_detail = 'valuesets:patient_mpi_match-detail'
        self.model = PatientMpiMatch
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestPayeetypeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestPayeetypeViewSet, self).setUp()
        self.url_list = reverse('valuesets:payeetype-list')
        self.url_detail = 'valuesets:payeetype-detail'
        self.model = Payeetype
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestPaymentAdjustmentReasonViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestPaymentAdjustmentReasonViewSet, self).setUp()
        self.url_list = reverse('valuesets:payment_adjustment_reason-list')
        self.url_detail = 'valuesets:payment_adjustment_reason-detail'
        self.model = PaymentAdjustmentReason
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestPaymentTypeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestPaymentTypeViewSet, self).setUp()
        self.url_list = reverse('valuesets:payment_type-list')
        self.url_detail = 'valuesets:payment_type-detail'
        self.model = PaymentType
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestPaymentStatusViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestPaymentStatusViewSet, self).setUp()
        self.url_list = reverse('valuesets:payment_status-list')
        self.url_detail = 'valuesets:payment_status-detail'
        self.model = PaymentStatus
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestPlanactionBehaviorTypeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestPlanactionBehaviorTypeViewSet, self).setUp()
        self.url_list = reverse('valuesets:planaction_behavior_type-list')
        self.url_detail = 'valuesets:planaction_behavior_type-detail'
        self.model = PlanactionBehaviorType
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestPlanactionRelationshipAnchorViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestPlanactionRelationshipAnchorViewSet, self).setUp()
        self.url_list = reverse('valuesets:planaction_relationship_anchor-list')
        self.url_detail = 'valuesets:planaction_relationship_anchor-detail'
        self.model = PlanactionRelationshipAnchor
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestPlanactionRelationshipTypeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestPlanactionRelationshipTypeViewSet, self).setUp()
        self.url_list = reverse('valuesets:planaction_relationship_type-list')
        self.url_detail = 'valuesets:planaction_relationship_type-detail'
        self.model = PlanactionRelationshipType
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestPlanactionTypeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestPlanactionTypeViewSet, self).setUp()
        self.url_list = reverse('valuesets:planaction_type-list')
        self.url_detail = 'valuesets:planaction_type-detail'
        self.model = PlanactionType
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestPractitionerRoleViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestPractitionerRoleViewSet, self).setUp()
        self.url_list = reverse('valuesets:practitioner_role-list')
        self.url_detail = 'valuesets:practitioner_role-detail'
        self.model = PractitionerRole
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestPractitionerSpecialtyViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestPractitionerSpecialtyViewSet, self).setUp()
        self.url_list = reverse('valuesets:practitioner_specialty-list')
        self.url_detail = 'valuesets:practitioner_specialty-detail'
        self.model = PractitionerSpecialty
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestPrecheckBehaviorViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestPrecheckBehaviorViewSet, self).setUp()
        self.url_list = reverse('valuesets:precheck_behavior-list')
        self.url_detail = 'valuesets:precheck_behavior-detail'
        self.model = PrecheckBehavior
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestProcedureProgressStatusCodesViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestProcedureProgressStatusCodesViewSet, self).setUp()
        self.url_list = reverse(
            'valuesets:procedure_progress_status_codes-list')
        self.url_detail = 'valuesets:procedure_progress_status_codes-detail'
        self.model = ProcedureProgressStatusCodes
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestProcedureRelationshipTypeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestProcedureRelationshipTypeViewSet, self).setUp()
        self.url_list = reverse('valuesets:procedure_relationship_type-list')
        self.url_detail = 'valuesets:procedure_relationship_type-detail'
        self.model = ProcedureRelationshipType
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestProcedureRequestPriorityViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestProcedureRequestPriorityViewSet, self).setUp()
        self.url_list = reverse('valuesets:procedure_request_priority-list')
        self.url_detail = 'valuesets:procedure_request_priority-detail'
        self.model = ProcedureRequestPriority
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestProcedureRequestStatusViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestProcedureRequestStatusViewSet, self).setUp()
        self.url_list = reverse('valuesets:procedure_request_status-list')
        self.url_detail = 'valuesets:procedure_request_status-detail'
        self.model = ProcedureRequestStatus
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestProcedureStatusViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestProcedureStatusViewSet, self).setUp()
        self.url_list = reverse('valuesets:procedure_status-list')
        self.url_detail = 'valuesets:procedure_status-detail'
        self.model = ProcedureStatus
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestProcessOutcomeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestProcessOutcomeViewSet, self).setUp()
        self.url_list = reverse('valuesets:process_outcome-list')
        self.url_detail = 'valuesets:process_outcome-detail'
        self.model = ProcessOutcome
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestProcessPriorityViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestProcessPriorityViewSet, self).setUp()
        self.url_list = reverse('valuesets:process_priority-list')
        self.url_detail = 'valuesets:process_priority-detail'
        self.model = ProcessPriority
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestPropertyRepresentationViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestPropertyRepresentationViewSet, self).setUp()
        self.url_list = reverse('valuesets:property_representation-list')
        self.url_detail = 'valuesets:property_representation-detail'
        self.model = PropertyRepresentation
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestProtocolActivityCategoryViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestProtocolActivityCategoryViewSet, self).setUp()
        self.url_list = reverse('valuesets:protocol_activity_category-list')
        self.url_detail = 'valuesets:protocol_activity_category-detail'
        self.model = ProtocolActivityCategory
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestProtocolStatusViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestProtocolStatusViewSet, self).setUp()
        self.url_list = reverse('valuesets:protocol_status-list')
        self.url_detail = 'valuesets:protocol_status-detail'
        self.model = ProtocolStatus
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestProtocolTypeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestProtocolTypeViewSet, self).setUp()
        self.url_list = reverse('valuesets:protocol_type-list')
        self.url_detail = 'valuesets:protocol_type-detail'
        self.model = ProtocolType
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestProvenanceEntityRoleViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestProvenanceEntityRoleViewSet, self).setUp()
        self.url_list = reverse('valuesets:provenance_entity_role-list')
        self.url_detail = 'valuesets:provenance_entity_role-detail'
        self.model = ProvenanceEntityRole
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestProvenanceAgentRoleViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestProvenanceAgentRoleViewSet, self).setUp()
        self.url_list = reverse('valuesets:provenance_agent_role-list')
        self.url_detail = 'valuesets:provenance_agent_role-detail'
        self.model = ProvenanceAgentRole
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestProvenanceAgentTypeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestProvenanceAgentTypeViewSet, self).setUp()
        self.url_list = reverse('valuesets:provenance_agent_type-list')
        self.url_detail = 'valuesets:provenance_agent_type-detail'
        self.model = ProvenanceAgentType
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestQuantityComparatorViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestQuantityComparatorViewSet, self).setUp()
        self.url_list = reverse('valuesets:quantity_comparator-list')
        self.url_detail = 'valuesets:quantity_comparator-detail'
        self.model = QuantityComparator
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestQuestionMaxOccursViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestQuestionMaxOccursViewSet, self).setUp()
        self.url_list = reverse('valuesets:question_max_occurs-list')
        self.url_detail = 'valuesets:question_max_occurs-detail'
        self.model = QuestionMaxOccurs
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestQuestionnaireAnswersStatusViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestQuestionnaireAnswersStatusViewSet, self).setUp()
        self.url_list = reverse('valuesets:questionnaire_answers_status-list')
        self.url_detail = 'valuesets:questionnaire_answers_status-detail'
        self.model = QuestionnaireAnswersStatus
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestQuestionnaireDisplayCategoryViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestQuestionnaireDisplayCategoryViewSet, self).setUp()
        self.url_list = reverse('valuesets:questionnaire_display_category-list')
        self.url_detail = 'valuesets:questionnaire_display_category-detail'
        self.model = QuestionnaireDisplayCategory
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestQuestionnaireItemControlViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestQuestionnaireItemControlViewSet, self).setUp()
        self.url_list = reverse('valuesets:questionnaire_item_control-list')
        self.url_detail = 'valuesets:questionnaire_item_control-detail'
        self.model = QuestionnaireItemControl
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestQuestionnaireStatusViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestQuestionnaireStatusViewSet, self).setUp()
        self.url_list = reverse('valuesets:questionnaire_status-list')
        self.url_detail = 'valuesets:questionnaire_status-detail'
        self.model = QuestionnaireStatus
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestReactionEventCertaintyViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestReactionEventCertaintyViewSet, self).setUp()
        self.url_list = reverse('valuesets:reaction_event_certainty-list')
        self.url_detail = 'valuesets:reaction_event_certainty-detail'
        self.model = ReactionEventCertainty
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestReactionEventSeverityViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestReactionEventSeverityViewSet, self).setUp()
        self.url_list = reverse('valuesets:reaction_event_severity-list')
        self.url_detail = 'valuesets:reaction_event_severity-detail'
        self.model = ReactionEventSeverity
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestReasonMedicationGivenCodesViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestReasonMedicationGivenCodesViewSet, self).setUp()
        self.url_list = reverse('valuesets:reason_medication_given_codes-list')
        self.url_detail = 'valuesets:reason_medication_given_codes-detail'
        self.model = ReasonMedicationGivenCodes
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestReasonMedicationNotGivenCodesViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestReasonMedicationNotGivenCodesViewSet, self).setUp()
        self.url_list = reverse(
            'valuesets:reason_medication_not_given_codes-list')
        self.url_detail = 'valuesets:reason_medication_not_given_codes-detail'
        self.model = ReasonMedicationNotGivenCodes
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestReferenceVersionRulesViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestReferenceVersionRulesViewSet, self).setUp()
        self.url_list = reverse('valuesets:reference_version_rules-list')
        self.url_detail = 'valuesets:reference_version_rules-detail'
        self.model = ReferenceVersionRules
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestReferencerangeMeaningViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestReferencerangeMeaningViewSet, self).setUp()
        self.url_list = reverse('valuesets:referencerange_meaning-list')
        self.url_detail = 'valuesets:referencerange_meaning-detail'
        self.model = ReferencerangeMeaning
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestReferralcategoryViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestReferralcategoryViewSet, self).setUp()
        self.url_list = reverse('valuesets:referralcategory-list')
        self.url_detail = 'valuesets:referralcategory-detail'
        self.model = Referralcategory
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestReferralstatusViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestReferralstatusViewSet, self).setUp()
        self.url_list = reverse('valuesets:referralstatus-list')
        self.url_detail = 'valuesets:referralstatus-detail'
        self.model = Referralstatus
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestRelationshipViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestRelationshipViewSet, self).setUp()
        self.url_list = reverse('valuesets:relationship-list')
        self.url_detail = 'valuesets:relationship-detail'
        self.model = Relationship
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestRemittanceOutcomeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestRemittanceOutcomeViewSet, self).setUp()
        self.url_list = reverse('valuesets:remittance_outcome-list')
        self.url_detail = 'valuesets:remittance_outcome-detail'
        self.model = RemittanceOutcome
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestRequiredBehaviorViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestRequiredBehaviorViewSet, self).setUp()
        self.url_list = reverse('valuesets:required_behavior-list')
        self.url_detail = 'valuesets:required_behavior-detail'
        self.model = RequiredBehavior
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestResourceAggregationModeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestResourceAggregationModeViewSet, self).setUp()
        self.url_list = reverse('valuesets:resource_aggregation_mode-list')
        self.url_detail = 'valuesets:resource_aggregation_mode-detail'
        self.model = ResourceAggregationMode
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestResourceSlicingRulesViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestResourceSlicingRulesViewSet, self).setUp()
        self.url_list = reverse('valuesets:resource_slicing_rules-list')
        self.url_detail = 'valuesets:resource_slicing_rules-detail'
        self.model = ResourceSlicingRules
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestResourceTypeLinkViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestResourceTypeLinkViewSet, self).setUp()
        self.url_list = reverse('valuesets:resource_type_link-list')
        self.url_detail = 'valuesets:resource_type_link-detail'
        self.model = ResourceTypeLink
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestResourceTypesViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestResourceTypesViewSet, self).setUp()
        self.url_list = reverse('valuesets:resource_types-list')
        self.url_detail = 'valuesets:resource_types-detail'
        self.model = ResourceTypes
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestResourceValidationModeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestResourceValidationModeViewSet, self).setUp()
        self.url_list = reverse('valuesets:resource_validation_mode-list')
        self.url_detail = 'valuesets:resource_validation_mode-detail'
        self.model = ResourceValidationMode
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestResponseCodeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestResponseCodeViewSet, self).setUp()
        self.url_list = reverse('valuesets:response_code-list')
        self.url_detail = 'valuesets:response_code-detail'
        self.model = ResponseCode
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestRestfulConformanceModeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestRestfulConformanceModeViewSet, self).setUp()
        self.url_list = reverse('valuesets:restful_conformance_mode-list')
        self.url_detail = 'valuesets:restful_conformance_mode-detail'
        self.model = RestfulConformanceMode
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestRestfulInteractionViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestRestfulInteractionViewSet, self).setUp()
        self.url_list = reverse('valuesets:restful_interaction-list')
        self.url_detail = 'valuesets:restful_interaction-detail'
        self.model = RestfulInteraction
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestRestfulSecurityServiceViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestRestfulSecurityServiceViewSet, self).setUp()
        self.url_list = reverse('valuesets:restful_security_service-list')
        self.url_detail = 'valuesets:restful_security_service-detail'
        self.model = RestfulSecurityService
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestRiskProbabilityViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestRiskProbabilityViewSet, self).setUp()
        self.url_list = reverse('valuesets:risk_probability-list')
        self.url_detail = 'valuesets:risk_probability-detail'
        self.model = RiskProbability
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestRulesetViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestRulesetViewSet, self).setUp()
        self.url_list = reverse('valuesets:ruleset-list')
        self.url_detail = 'valuesets:ruleset-detail'
        self.model = Ruleset
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestSearchEntryModeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestSearchEntryModeViewSet, self).setUp()
        self.url_list = reverse('valuesets:search_entry_mode-list')
        self.url_detail = 'valuesets:search_entry_mode-detail'
        self.model = SearchEntryMode
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestSearchModifierCodeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestSearchModifierCodeViewSet, self).setUp()
        self.url_list = reverse('valuesets:search_modifier_code-list')
        self.url_detail = 'valuesets:search_modifier_code-detail'
        self.model = SearchModifierCode
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestSearchParamTypeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestSearchParamTypeViewSet, self).setUp()
        self.url_list = reverse('valuesets:search_param_type-list')
        self.url_detail = 'valuesets:search_param_type-detail'
        self.model = SearchParamType
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestSearchXpathUsageViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestSearchXpathUsageViewSet, self).setUp()
        self.url_list = reverse('valuesets:search_xpath_usage-list')
        self.url_detail = 'valuesets:search_xpath_usage-detail'
        self.model = SearchXpathUsage
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestAuditSourceTypeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestAuditSourceTypeViewSet, self).setUp()
        self.url_list = reverse('valuesets:audit_source_type-list')
        self.url_detail = 'valuesets:audit_source_type-detail'
        self.model = AuditSourceType
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestSelectionBehaviorViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestSelectionBehaviorViewSet, self).setUp()
        self.url_list = reverse('valuesets:selection_behavior-list')
        self.url_detail = 'valuesets:selection_behavior-detail'
        self.model = SelectionBehavior
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestSequenceTypeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestSequenceTypeViewSet, self).setUp()
        self.url_list = reverse('valuesets:sequence_type-list')
        self.url_detail = 'valuesets:sequence_type-detail'
        self.model = SequenceType
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestServiceCategoryViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestServiceCategoryViewSet, self).setUp()
        self.url_list = reverse('valuesets:service_category-list')
        self.url_detail = 'valuesets:service_category-detail'
        self.model = ServiceCategory
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestServiceProvisionConditionsViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestServiceProvisionConditionsViewSet, self).setUp()
        self.url_list = reverse('valuesets:service_provision_conditions-list')
        self.url_detail = 'valuesets:service_provision_conditions-detail'
        self.model = ServiceProvisionConditions
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestServiceReferralMethodViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestServiceReferralMethodViewSet, self).setUp()
        self.url_list = reverse('valuesets:service_referral_method-list')
        self.url_detail = 'valuesets:service_referral_method-detail'
        self.model = ServiceReferralMethod
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestServiceTypeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestServiceTypeViewSet, self).setUp()
        self.url_list = reverse('valuesets:service_type-list')
        self.url_detail = 'valuesets:service_type-detail'
        self.model = ServiceType
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestIcd10ProceduresViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestIcd10ProceduresViewSet, self).setUp()
        self.url_list = reverse('valuesets:icd_10_procedures-list')
        self.url_detail = 'valuesets:icd_10_procedures-detail'
        self.model = Icd10Procedures
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestSlotstatusViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestSlotstatusViewSet, self).setUp()
        self.url_list = reverse('valuesets:slotstatus-list')
        self.url_detail = 'valuesets:slotstatus-detail'
        self.model = Slotstatus
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestSpecialValuesViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestSpecialValuesViewSet, self).setUp()
        self.url_list = reverse('valuesets:special_values-list')
        self.url_detail = 'valuesets:special_values-detail'
        self.model = SpecialValues
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestSpecimenStatusViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestSpecimenStatusViewSet, self).setUp()
        self.url_list = reverse('valuesets:specimen_status-list')
        self.url_detail = 'valuesets:specimen_status-detail'
        self.model = SpecimenStatus
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestStructureDefinitionKindViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestStructureDefinitionKindViewSet, self).setUp()
        self.url_list = reverse('valuesets:structure_definition_kind-list')
        self.url_detail = 'valuesets:structure_definition_kind-detail'
        self.model = StructureDefinitionKind
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestSubscriptionChannelTypeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestSubscriptionChannelTypeViewSet, self).setUp()
        self.url_list = reverse('valuesets:subscription_channel_type-list')
        self.url_detail = 'valuesets:subscription_channel_type-detail'
        self.model = SubscriptionChannelType
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestSubscriptionStatusViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestSubscriptionStatusViewSet, self).setUp()
        self.url_list = reverse('valuesets:subscription_status-list')
        self.url_detail = 'valuesets:subscription_status-detail'
        self.model = SubscriptionStatus
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestSubscriptionTagViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestSubscriptionTagViewSet, self).setUp()
        self.url_list = reverse('valuesets:subscription_tag-list')
        self.url_detail = 'valuesets:subscription_tag-detail'
        self.model = SubscriptionTag
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestSubstanceCategoryViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestSubstanceCategoryViewSet, self).setUp()
        self.url_list = reverse('valuesets:substance_category-list')
        self.url_detail = 'valuesets:substance_category-detail'
        self.model = SubstanceCategory
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestSupplydeliveryTypeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestSupplydeliveryTypeViewSet, self).setUp()
        self.url_list = reverse('valuesets:supplydelivery_type-list')
        self.url_detail = 'valuesets:supplydelivery_type-detail'
        self.model = SupplydeliveryType
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestSupplyrequestKindViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestSupplyrequestKindViewSet, self).setUp()
        self.url_list = reverse('valuesets:supplyrequest_kind-list')
        self.url_detail = 'valuesets:supplyrequest_kind-detail'
        self.model = SupplyrequestKind
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestSupplydeliveryStatusViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestSupplydeliveryStatusViewSet, self).setUp()
        self.url_list = reverse('valuesets:supplydelivery_status-list')
        self.url_detail = 'valuesets:supplydelivery_status-detail'
        self.model = SupplydeliveryStatus
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestSupplyrequestReasonViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestSupplyrequestReasonViewSet, self).setUp()
        self.url_list = reverse('valuesets:supplyrequest_reason-list')
        self.url_detail = 'valuesets:supplyrequest_reason-detail'
        self.model = SupplyrequestReason
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestSupplyrequestStatusViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestSupplyrequestStatusViewSet, self).setUp()
        self.url_list = reverse('valuesets:supplyrequest_status-list')
        self.url_detail = 'valuesets:supplyrequest_status-detail'
        self.model = SupplyrequestStatus
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestTaskPerformerTypeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestTaskPerformerTypeViewSet, self).setUp()
        self.url_list = reverse('valuesets:task_performer_type-list')
        self.url_detail = 'valuesets:task_performer_type-detail'
        self.model = TaskPerformerType
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestTaskPriorityViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestTaskPriorityViewSet, self).setUp()
        self.url_list = reverse('valuesets:task_priority-list')
        self.url_detail = 'valuesets:task_priority-detail'
        self.model = TaskPriority
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestTaskStageViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestTaskStageViewSet, self).setUp()
        self.url_list = reverse('valuesets:task_stage-list')
        self.url_detail = 'valuesets:task_stage-detail'
        self.model = TaskStage
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestTaskStatusViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestTaskStatusViewSet, self).setUp()
        self.url_list = reverse('valuesets:task_status-list')
        self.url_detail = 'valuesets:task_status-detail'
        self.model = TaskStatus
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestTestscriptOperationCodesViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestTestscriptOperationCodesViewSet, self).setUp()
        self.url_list = reverse('valuesets:testscript_operation_codes-list')
        self.url_detail = 'valuesets:testscript_operation_codes-detail'
        self.model = TestscriptOperationCodes
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestTestscriptProfileDestinationTypesViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestTestscriptProfileDestinationTypesViewSet, self).setUp()
        self.url_list = reverse(
            'valuesets:testscript_profile_destination_types-list')
        self.url_detail = (
            'valuesets:testscript_profile_destination_types-detail')
        self.model = TestscriptProfileDestinationTypes
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestTestscriptProfileOriginTypesViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestTestscriptProfileOriginTypesViewSet, self).setUp()
        self.url_list = reverse(
            'valuesets:testscript_profile_origin_types-list')
        self.url_detail = 'valuesets:testscript_profile_origin_types-detail'
        self.model = TestscriptProfileOriginTypes
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestTransactionModeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestTransactionModeViewSet, self).setUp()
        self.url_list = reverse('valuesets:transaction_mode-list')
        self.url_detail = 'valuesets:transaction_mode-detail'
        self.model = TransactionMode
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestTriggerTypeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestTriggerTypeViewSet, self).setUp()
        self.url_list = reverse('valuesets:trigger_type-list')
        self.url_detail = 'valuesets:trigger_type-detail'
        self.model = TriggerType
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestTypeDerivationRuleViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestTypeDerivationRuleViewSet, self).setUp()
        self.url_list = reverse('valuesets:type_derivation_rule-list')
        self.url_detail = 'valuesets:type_derivation_rule-detail'
        self.model = TypeDerivationRule
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestUnknownContentCodeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestUnknownContentCodeViewSet, self).setUp()
        self.url_list = reverse('valuesets:unknown_content_code-list')
        self.url_detail = 'valuesets:unknown_content_code-detail'
        self.model = UnknownContentCode
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestVaccinationProtocolDoseStatusViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestVaccinationProtocolDoseStatusViewSet, self).setUp()
        self.url_list = reverse(
            'valuesets:vaccination_protocol_dose_status-list')
        self.url_detail = 'valuesets:vaccination_protocol_dose_status-detail'
        self.model = VaccinationProtocolDoseStatus
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestVaccinationProtocolDoseStatusReasonViewSet(
        APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestVaccinationProtocolDoseStatusReasonViewSet, self).setUp()
        self.url_list = reverse(
            'valuesets:vaccination_protocol_dose_status_reason-list')
        self.url_detail = (
            'valuesets:vaccination_protocol_dose_status_reason-detail')
        self.model = VaccinationProtocolDoseStatusReason
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestVariantStateViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestVariantStateViewSet, self).setUp()
        self.url_list = reverse('valuesets:variant_state-list')
        self.url_detail = 'valuesets:variant_state-detail'
        self.model = VariantState
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestVersioningPolicyViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestVersioningPolicyViewSet, self).setUp()
        self.url_list = reverse('valuesets:versioning_policy-list')
        self.url_detail = 'valuesets:versioning_policy-detail'
        self.model = VersioningPolicy
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestVisionBaseCodesViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestVisionBaseCodesViewSet, self).setUp()
        self.url_list = reverse('valuesets:vision_base_codes-list')
        self.url_detail = 'valuesets:vision_base_codes-detail'
        self.model = VisionBaseCodes
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestVisionEyeCodesViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestVisionEyeCodesViewSet, self).setUp()
        self.url_list = reverse('valuesets:vision_eye_codes-list')
        self.url_detail = 'valuesets:vision_eye_codes-detail'
        self.model = VisionEyeCodes
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestXdsRelationshipTypeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestXdsRelationshipTypeViewSet, self).setUp()
        self.url_list = reverse('valuesets:xds_relationship_type-list')
        self.url_detail = 'valuesets:xds_relationship_type-detail'
        self.model = XdsRelationshipType
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestAcknowledgementconditionViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestAcknowledgementconditionViewSet, self).setUp()
        self.url_list = reverse('valuesets:AcknowledgementCondition-list')
        self.url_detail = 'valuesets:AcknowledgementCondition-detail'
        self.model = Acknowledgementcondition
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestAcknowledgementdetailcodeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestAcknowledgementdetailcodeViewSet, self).setUp()
        self.url_list = reverse('valuesets:AcknowledgementDetailCode-list')
        self.url_detail = 'valuesets:AcknowledgementDetailCode-detail'
        self.model = Acknowledgementdetailcode
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestAcknowledgementdetailtypeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestAcknowledgementdetailtypeViewSet, self).setUp()
        self.url_list = reverse('valuesets:AcknowledgementDetailType-list')
        self.url_detail = 'valuesets:AcknowledgementDetailType-detail'
        self.model = Acknowledgementdetailtype
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestAcknowledgementtypeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestAcknowledgementtypeViewSet, self).setUp()
        self.url_list = reverse('valuesets:AcknowledgementType-list')
        self.url_detail = 'valuesets:AcknowledgementType-detail'
        self.model = Acknowledgementtype
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestActclassViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestActclassViewSet, self).setUp()
        self.url_list = reverse('valuesets:ActClass-list')
        self.url_detail = 'valuesets:ActClass-detail'
        self.model = Actclass
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestActcodeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestActcodeViewSet, self).setUp()
        self.url_list = reverse('valuesets:ActCode-list')
        self.url_detail = 'valuesets:ActCode-detail'
        self.model = Actcode
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestActexposurelevelcodeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestActexposurelevelcodeViewSet, self).setUp()
        self.url_list = reverse('valuesets:ActExposureLevelCode-list')
        self.url_detail = 'valuesets:ActExposureLevelCode-detail'
        self.model = Actexposurelevelcode
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestActinvoiceelementmodifierViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestActinvoiceelementmodifierViewSet, self).setUp()
        self.url_list = reverse('valuesets:ActInvoiceElementModifier-list')
        self.url_detail = 'valuesets:ActInvoiceElementModifier-detail'
        self.model = Actinvoiceelementmodifier
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestActmoodViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestActmoodViewSet, self).setUp()
        self.url_list = reverse('valuesets:ActMood-list')
        self.url_detail = 'valuesets:ActMood-detail'
        self.model = Actmood
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestActpriorityViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestActpriorityViewSet, self).setUp()
        self.url_list = reverse('valuesets:ActPriority-list')
        self.url_detail = 'valuesets:ActPriority-detail'
        self.model = Actpriority
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestActreasonViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestActreasonViewSet, self).setUp()
        self.url_list = reverse('valuesets:ActReason-list')
        self.url_detail = 'valuesets:ActReason-detail'
        self.model = Actreason
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestActrelationshipcheckpointViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestActrelationshipcheckpointViewSet, self).setUp()
        self.url_list = reverse('valuesets:ActRelationshipCheckpoint-list')
        self.url_detail = 'valuesets:ActRelationshipCheckpoint-detail'
        self.model = Actrelationshipcheckpoint
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestActrelationshipjoinViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestActrelationshipjoinViewSet, self).setUp()
        self.url_list = reverse('valuesets:ActRelationshipJoin-list')
        self.url_detail = 'valuesets:ActRelationshipJoin-detail'
        self.model = Actrelationshipjoin
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestActrelationshipsplitViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestActrelationshipsplitViewSet, self).setUp()
        self.url_list = reverse('valuesets:ActRelationshipSplit-list')
        self.url_detail = 'valuesets:ActRelationshipSplit-detail'
        self.model = Actrelationshipsplit
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestActrelationshipsubsetViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestActrelationshipsubsetViewSet, self).setUp()
        self.url_list = reverse('valuesets:ActRelationshipSubset-list')
        self.url_detail = 'valuesets:ActRelationshipSubset-detail'
        self.model = Actrelationshipsubset
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestActrelationshiptypeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestActrelationshiptypeViewSet, self).setUp()
        self.url_list = reverse('valuesets:ActRelationshipType-list')
        self.url_detail = 'valuesets:ActRelationshipType-detail'
        self.model = Actrelationshiptype
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestActsiteViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestActsiteViewSet, self).setUp()
        self.url_list = reverse('valuesets:ActSite-list')
        self.url_detail = 'valuesets:ActSite-detail'
        self.model = Actsite
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestActstatusViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestActstatusViewSet, self).setUp()
        self.url_list = reverse('valuesets:ActStatus-list')
        self.url_detail = 'valuesets:ActStatus-detail'
        self.model = Actstatus
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestActusprivacylawViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestActusprivacylawViewSet, self).setUp()
        self.url_list = reverse('valuesets:ActUSPrivacyLaw-list')
        self.url_detail = 'valuesets:ActUSPrivacyLaw-detail'
        self.model = Actusprivacylaw
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestActuncertaintyViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestActuncertaintyViewSet, self).setUp()
        self.url_list = reverse('valuesets:ActUncertainty-list')
        self.url_detail = 'valuesets:ActUncertainty-detail'
        self.model = Actuncertainty
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestAddressparttypeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestAddressparttypeViewSet, self).setUp()
        self.url_list = reverse('valuesets:AddressPartType-list')
        self.url_detail = 'valuesets:AddressPartType-detail'
        self.model = Addressparttype
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestAmericanindianalaskanativelanguagesViewSet(
        APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestAmericanindianalaskanativelanguagesViewSet, self).setUp()
        self.url_list = reverse(
            'valuesets:AmericanIndianAlaskaNativeLanguages-list')
        self.url_detail = 'valuesets:AmericanIndianAlaskaNativeLanguages-detail'
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
        self.url_list = reverse('valuesets:CalendarCycle-list')
        self.url_detail = 'valuesets:CalendarCycle-detail'
        self.model = Calendarcycle
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestCalendartypeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestCalendartypeViewSet, self).setUp()
        self.url_list = reverse('valuesets:CalendarType-list')
        self.url_detail = 'valuesets:CalendarType-detail'
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
        self.url_list = reverse('valuesets:CodingRationale-list')
        self.url_detail = 'valuesets:CodingRationale-detail'
        self.model = Codingrationale
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestCommunicationfunctiontypeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestCommunicationfunctiontypeViewSet, self).setUp()
        self.url_list = reverse('valuesets:CommunicationFunctionType-list')
        self.url_detail = 'valuesets:CommunicationFunctionType-detail'
        self.model = Communicationfunctiontype
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestCompressionalgorithmViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestCompressionalgorithmViewSet, self).setUp()
        self.url_list = reverse('valuesets:CompressionAlgorithm-list')
        self.url_detail = 'valuesets:CompressionAlgorithm-detail'
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
        self.url_list = reverse('valuesets:ContainerCap-list')
        self.url_detail = 'valuesets:ContainerCap-detail'
        self.model = Containercap
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestContainerseparatorViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestContainerseparatorViewSet, self).setUp()
        self.url_list = reverse('valuesets:ContainerSeparator-list')
        self.url_detail = 'valuesets:ContainerSeparator-detail'
        self.model = Containerseparator
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestContentprocessingmodeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestContentprocessingmodeViewSet, self).setUp()
        self.url_list = reverse('valuesets:ContentProcessingMode-list')
        self.url_detail = 'valuesets:ContentProcessingMode-detail'
        self.model = Contentprocessingmode
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestContextcontrolViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestContextcontrolViewSet, self).setUp()
        self.url_list = reverse('valuesets:ContextControl-list')
        self.url_detail = 'valuesets:ContextControl-detail'
        self.model = Contextcontrol
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestDataoperationViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestDataoperationViewSet, self).setUp()
        self.url_list = reverse('valuesets:DataOperation-list')
        self.url_detail = 'valuesets:DataOperation-detail'
        self.model = Dataoperation
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestDevicealertlevelViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestDevicealertlevelViewSet, self).setUp()
        self.url_list = reverse('valuesets:DeviceAlertLevel-list')
        self.url_detail = 'valuesets:DeviceAlertLevel-detail'
        self.model = Devicealertlevel
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestDocumentcompletionViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestDocumentcompletionViewSet, self).setUp()
        self.url_list = reverse('valuesets:DocumentCompletion-list')
        self.url_detail = 'valuesets:DocumentCompletion-detail'
        self.model = Documentcompletion
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestDocumentstorageViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestDocumentstorageViewSet, self).setUp()
        self.url_list = reverse('valuesets:DocumentStorage-list')
        self.url_detail = 'valuesets:DocumentStorage-detail'
        self.model = Documentstorage
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestEducationlevelViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestEducationlevelViewSet, self).setUp()
        self.url_list = reverse('valuesets:EducationLevel-list')
        self.url_detail = 'valuesets:EducationLevel-detail'
        self.model = Educationlevel
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestEmployeejobclassViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestEmployeejobclassViewSet, self).setUp()
        self.url_list = reverse('valuesets:EmployeeJobClass-list')
        self.url_detail = 'valuesets:EmployeeJobClass-detail'
        self.model = Employeejobclass
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestEncounteradmissionsourceViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestEncounteradmissionsourceViewSet, self).setUp()
        self.url_list = reverse('valuesets:EncounterAdmissionSource-list')
        self.url_detail = 'valuesets:EncounterAdmissionSource-detail'
        self.model = Encounteradmissionsource
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestEncounterspecialcourtesyViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestEncounterspecialcourtesyViewSet, self).setUp()
        self.url_list = reverse('valuesets:EncounterSpecialCourtesy-list')
        self.url_detail = 'valuesets:EncounterSpecialCourtesy-detail'
        self.model = Encounterspecialcourtesy
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestEntityclassViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestEntityclassViewSet, self).setUp()
        self.url_list = reverse('valuesets:EntityClass-list')
        self.url_detail = 'valuesets:EntityClass-detail'
        self.model = Entityclass
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestEntitycodeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestEntitycodeViewSet, self).setUp()
        self.url_list = reverse('valuesets:EntityCode-list')
        self.url_detail = 'valuesets:EntityCode-detail'
        self.model = Entitycode
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestEntitydeterminerViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestEntitydeterminerViewSet, self).setUp()
        self.url_list = reverse('valuesets:EntityDeterminer-list')
        self.url_detail = 'valuesets:EntityDeterminer-detail'
        self.model = Entitydeterminer
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestEntityhandlingViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestEntityhandlingViewSet, self).setUp()
        self.url_list = reverse('valuesets:EntityHandling-list')
        self.url_detail = 'valuesets:EntityHandling-detail'
        self.model = Entityhandling
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestEntitynamepartqualifierViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestEntitynamepartqualifierViewSet, self).setUp()
        self.url_list = reverse('valuesets:EntityNamePartQualifier-list')
        self.url_detail = 'valuesets:EntityNamePartQualifier-detail'
        self.model = Entitynamepartqualifier
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestEntitynamepartqualifierr2ViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestEntitynamepartqualifierr2ViewSet, self).setUp()
        self.url_list = reverse('valuesets:EntityNamePartQualifierR2-list')
        self.url_detail = 'valuesets:EntityNamePartQualifierR2-detail'
        self.model = Entitynamepartqualifierr2
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestEntitynameparttypeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestEntitynameparttypeViewSet, self).setUp()
        self.url_list = reverse('valuesets:EntityNamePartType-list')
        self.url_detail = 'valuesets:EntityNamePartType-detail'
        self.model = Entitynameparttype
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestEntitynameparttyper2ViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestEntitynameparttyper2ViewSet, self).setUp()
        self.url_list = reverse('valuesets:EntityNamePartTypeR2-list')
        self.url_detail = 'valuesets:EntityNamePartTypeR2-detail'
        self.model = Entitynameparttyper2
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestEntitynameuseViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestEntitynameuseViewSet, self).setUp()
        self.url_list = reverse('valuesets:EntityNameUse-list')
        self.url_detail = 'valuesets:EntityNameUse-detail'
        self.model = Entitynameuse
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestEntitynameuser2ViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestEntitynameuser2ViewSet, self).setUp()
        self.url_list = reverse('valuesets:EntityNameUseR2-list')
        self.url_detail = 'valuesets:EntityNameUseR2-detail'
        self.model = Entitynameuser2
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestEntityriskViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestEntityriskViewSet, self).setUp()
        self.url_list = reverse('valuesets:EntityRisk-list')
        self.url_detail = 'valuesets:EntityRisk-detail'
        self.model = Entityrisk
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestEntitystatusViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestEntitystatusViewSet, self).setUp()
        self.url_list = reverse('valuesets:EntityStatus-list')
        self.url_detail = 'valuesets:EntityStatus-detail'
        self.model = Entitystatus
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestEquipmentalertlevelViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestEquipmentalertlevelViewSet, self).setUp()
        self.url_list = reverse('valuesets:EquipmentAlertLevel-list')
        self.url_detail = 'valuesets:EquipmentAlertLevel-detail'
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
        self.url_list = reverse('valuesets:ExposureMode-list')
        self.url_detail = 'valuesets:ExposureMode-detail'
        self.model = Exposuremode
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestGtsabbreviationViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestGtsabbreviationViewSet, self).setUp()
        self.url_list = reverse('valuesets:GTSAbbreviation-list')
        self.url_detail = 'valuesets:GTSAbbreviation-detail'
        self.model = Gtsabbreviation
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestGenderstatusViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestGenderstatusViewSet, self).setUp()
        self.url_list = reverse('valuesets:GenderStatus-list')
        self.url_detail = 'valuesets:GenderStatus-detail'
        self.model = Genderstatus
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestHl7updatemodeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestHl7updatemodeViewSet, self).setUp()
        self.url_list = reverse('valuesets:HL7UpdateMode-list')
        self.url_detail = 'valuesets:HL7UpdateMode-detail'
        self.model = Hl7updatemode
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestHtmllinktypeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestHtmllinktypeViewSet, self).setUp()
        self.url_list = reverse('valuesets:HtmlLinkType-list')
        self.url_detail = 'valuesets:HtmlLinkType-detail'
        self.model = Htmllinktype
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestIdentifierreliabilityViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestIdentifierreliabilityViewSet, self).setUp()
        self.url_list = reverse('valuesets:IdentifierReliability-list')
        self.url_detail = 'valuesets:IdentifierReliability-detail'
        self.model = Identifierreliability
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestIdentifierscopeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestIdentifierscopeViewSet, self).setUp()
        self.url_list = reverse('valuesets:IdentifierScope-list')
        self.url_detail = 'valuesets:IdentifierScope-detail'
        self.model = Identifierscope
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestIntegritycheckalgorithmViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestIntegritycheckalgorithmViewSet, self).setUp()
        self.url_list = reverse('valuesets:IntegrityCheckAlgorithm-list')
        self.url_detail = 'valuesets:IntegrityCheckAlgorithm-detail'
        self.model = Integritycheckalgorithm
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestLanguageabilitymodeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestLanguageabilitymodeViewSet, self).setUp()
        self.url_list = reverse('valuesets:LanguageAbilityMode-list')
        self.url_detail = 'valuesets:LanguageAbilityMode-detail'
        self.model = Languageabilitymode
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestLanguageabilityproficiencyViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestLanguageabilityproficiencyViewSet, self).setUp()
        self.url_list = reverse('valuesets:LanguageAbilityProficiency-list')
        self.url_detail = 'valuesets:LanguageAbilityProficiency-detail'
        self.model = Languageabilityproficiency
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestLivingarrangementViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestLivingarrangementViewSet, self).setUp()
        self.url_list = reverse('valuesets:LivingArrangement-list')
        self.url_detail = 'valuesets:LivingArrangement-detail'
        self.model = Livingarrangement
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestLocalmarkupignoreViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestLocalmarkupignoreViewSet, self).setUp()
        self.url_list = reverse('valuesets:LocalMarkupIgnore-list')
        self.url_detail = 'valuesets:LocalMarkupIgnore-detail'
        self.model = Localmarkupignore
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestLocalremotecontrolstateViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestLocalremotecontrolstateViewSet, self).setUp()
        self.url_list = reverse('valuesets:LocalRemoteControlState-list')
        self.url_detail = 'valuesets:LocalRemoteControlState-detail'
        self.model = Localremotecontrolstate
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestManagedparticipationstatusViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestManagedparticipationstatusViewSet, self).setUp()
        self.url_list = reverse('valuesets:ManagedParticipationStatus-list')
        self.url_detail = 'valuesets:ManagedParticipationStatus-detail'
        self.model = Managedparticipationstatus
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestMaprelationshipViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestMaprelationshipViewSet, self).setUp()
        self.url_list = reverse('valuesets:MapRelationship-list')
        self.url_detail = 'valuesets:MapRelationship-detail'
        self.model = Maprelationship
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestMessagewaitingpriorityViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestMessagewaitingpriorityViewSet, self).setUp()
        self.url_list = reverse('valuesets:MessageWaitingPriority-list')
        self.url_detail = 'valuesets:MessageWaitingPriority-detail'
        self.model = Messagewaitingpriority
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestModifyindicatorViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestModifyindicatorViewSet, self).setUp()
        self.url_list = reverse('valuesets:ModifyIndicator-list')
        self.url_detail = 'valuesets:ModifyIndicator-detail'
        self.model = Modifyindicator
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestNullflavorViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestNullflavorViewSet, self).setUp()
        self.url_list = reverse('valuesets:NullFlavor-list')
        self.url_detail = 'valuesets:NullFlavor-detail'
        self.model = Nullflavor
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestObservationinterpretationViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestObservationinterpretationViewSet, self).setUp()
        self.url_list = reverse('valuesets:ObservationInterpretation-list')
        self.url_detail = 'valuesets:ObservationInterpretation-detail'
        self.model = Observationinterpretation
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestObservationmethodViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestObservationmethodViewSet, self).setUp()
        self.url_list = reverse('valuesets:ObservationMethod-list')
        self.url_detail = 'valuesets:ObservationMethod-detail'
        self.model = Observationmethod
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestObservationvalueViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestObservationvalueViewSet, self).setUp()
        self.url_list = reverse('valuesets:ObservationValue-list')
        self.url_detail = 'valuesets:ObservationValue-detail'
        self.model = Observationvalue
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestParticipationfunctionViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestParticipationfunctionViewSet, self).setUp()
        self.url_list = reverse('valuesets:ParticipationFunction-list')
        self.url_detail = 'valuesets:ParticipationFunction-detail'
        self.model = Participationfunction
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestParticipationmodeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestParticipationmodeViewSet, self).setUp()
        self.url_list = reverse('valuesets:ParticipationMode-list')
        self.url_detail = 'valuesets:ParticipationMode-detail'
        self.model = Participationmode
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestParticipationsignatureViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestParticipationsignatureViewSet, self).setUp()
        self.url_list = reverse('valuesets:ParticipationSignature-list')
        self.url_detail = 'valuesets:ParticipationSignature-detail'
        self.model = Participationsignature
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestParticipationtypeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestParticipationtypeViewSet, self).setUp()
        self.url_list = reverse('valuesets:ParticipationType-list')
        self.url_detail = 'valuesets:ParticipationType-detail'
        self.model = Participationtype
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestPatientimportanceViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestPatientimportanceViewSet, self).setUp()
        self.url_list = reverse('valuesets:PatientImportance-list')
        self.url_detail = 'valuesets:PatientImportance-detail'
        self.model = Patientimportance
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestPaymenttermsViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestPaymenttermsViewSet, self).setUp()
        self.url_list = reverse('valuesets:PaymentTerms-list')
        self.url_detail = 'valuesets:PaymentTerms-detail'
        self.model = Paymentterms
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestPersondisabilitytypeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestPersondisabilitytypeViewSet, self).setUp()
        self.url_list = reverse('valuesets:PersonDisabilityType-list')
        self.url_detail = 'valuesets:PersonDisabilityType-detail'
        self.model = Persondisabilitytype
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestProbabilitydistributiontypeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestProbabilitydistributiontypeViewSet, self).setUp()
        self.url_list = reverse('valuesets:ProbabilityDistributionType-list')
        self.url_detail = 'valuesets:ProbabilityDistributionType-detail'
        self.model = Probabilitydistributiontype
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestProcessingidViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestProcessingidViewSet, self).setUp()
        self.url_list = reverse('valuesets:ProcessingID-list')
        self.url_detail = 'valuesets:ProcessingID-detail'
        self.model = Processingid
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestProcessingmodeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestProcessingmodeViewSet, self).setUp()
        self.url_list = reverse('valuesets:ProcessingMode-list')
        self.url_detail = 'valuesets:ProcessingMode-detail'
        self.model = Processingmode
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestQueryparametervalueViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestQueryparametervalueViewSet, self).setUp()
        self.url_list = reverse('valuesets:QueryParameterValue-list')
        self.url_detail = 'valuesets:QueryParameterValue-detail'
        self.model = Queryparametervalue
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestQuerypriorityViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestQuerypriorityViewSet, self).setUp()
        self.url_list = reverse('valuesets:QueryPriority-list')
        self.url_detail = 'valuesets:QueryPriority-detail'
        self.model = Querypriority
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestQueryrequestlimitViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestQueryrequestlimitViewSet, self).setUp()
        self.url_list = reverse('valuesets:QueryRequestLimit-list')
        self.url_detail = 'valuesets:QueryRequestLimit-detail'
        self.model = Queryrequestlimit
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestQueryresponseViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestQueryresponseViewSet, self).setUp()
        self.url_list = reverse('valuesets:QueryResponse-list')
        self.url_detail = 'valuesets:QueryResponse-detail'
        self.model = Queryresponse
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestQuerystatuscodeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestQuerystatuscodeViewSet, self).setUp()
        self.url_list = reverse('valuesets:QueryStatusCode-list')
        self.url_detail = 'valuesets:QueryStatusCode-detail'
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
        self.url_list = reverse('valuesets:RelationalOperator-list')
        self.url_detail = 'valuesets:RelationalOperator-detail'
        self.model = Relationaloperator
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestRelationshipconjunctionViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestRelationshipconjunctionViewSet, self).setUp()
        self.url_list = reverse('valuesets:RelationshipConjunction-list')
        self.url_detail = 'valuesets:RelationshipConjunction-detail'
        self.model = Relationshipconjunction
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestReligiousaffiliationViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestReligiousaffiliationViewSet, self).setUp()
        self.url_list = reverse('valuesets:ReligiousAffiliation-list')
        self.url_detail = 'valuesets:ReligiousAffiliation-detail'
        self.model = Religiousaffiliation
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestResponselevelViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestResponselevelViewSet, self).setUp()
        self.url_list = reverse('valuesets:ResponseLevel-list')
        self.url_detail = 'valuesets:ResponseLevel-detail'
        self.model = Responselevel
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestResponsemodalityViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestResponsemodalityViewSet, self).setUp()
        self.url_list = reverse('valuesets:ResponseModality-list')
        self.url_detail = 'valuesets:ResponseModality-detail'
        self.model = Responsemodality
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestResponsemodeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestResponsemodeViewSet, self).setUp()
        self.url_list = reverse('valuesets:ResponseMode-list')
        self.url_detail = 'valuesets:ResponseMode-detail'
        self.model = Responsemode
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestRoleclassViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestRoleclassViewSet, self).setUp()
        self.url_list = reverse('valuesets:RoleClass-list')
        self.url_detail = 'valuesets:RoleClass-detail'
        self.model = Roleclass
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestRolecodeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestRolecodeViewSet, self).setUp()
        self.url_list = reverse('valuesets:RoleCode-list')
        self.url_detail = 'valuesets:RoleCode-detail'
        self.model = Rolecode
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestRolelinkstatusViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestRolelinkstatusViewSet, self).setUp()
        self.url_list = reverse('valuesets:RoleLinkStatus-list')
        self.url_detail = 'valuesets:RoleLinkStatus-detail'
        self.model = Rolelinkstatus
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestRolelinktypeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestRolelinktypeViewSet, self).setUp()
        self.url_list = reverse('valuesets:RoleLinkType-list')
        self.url_detail = 'valuesets:RoleLinkType-detail'
        self.model = Rolelinktype
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestRolestatusViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestRolestatusViewSet, self).setUp()
        self.url_list = reverse('valuesets:RoleStatus-list')
        self.url_detail = 'valuesets:RoleStatus-detail'
        self.model = Rolestatus
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestRouteofadministrationViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestRouteofadministrationViewSet, self).setUp()
        self.url_list = reverse('valuesets:RouteOfAdministration-list')
        self.url_detail = 'valuesets:RouteOfAdministration-detail'
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
        self.url_list = reverse('valuesets:SetOperator-list')
        self.url_detail = 'valuesets:SetOperator-detail'
        self.model = Setoperator
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestSpecimentypeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestSpecimentypeViewSet, self).setUp()
        self.url_list = reverse('valuesets:SpecimenType-list')
        self.url_detail = 'valuesets:SpecimenType-detail'
        self.model = Specimentype
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestSubstitutionconditionViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestSubstitutionconditionViewSet, self).setUp()
        self.url_list = reverse('valuesets:SubstitutionCondition-list')
        self.url_detail = 'valuesets:SubstitutionCondition-detail'
        self.model = Substitutioncondition
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestTablecellhorizontalalignViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestTablecellhorizontalalignViewSet, self).setUp()
        self.url_list = reverse('valuesets:TableCellHorizontalAlign-list')
        self.url_detail = 'valuesets:TableCellHorizontalAlign-detail'
        self.model = Tablecellhorizontalalign
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestTablecellscopeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestTablecellscopeViewSet, self).setUp()
        self.url_list = reverse('valuesets:TableCellScope-list')
        self.url_detail = 'valuesets:TableCellScope-detail'
        self.model = Tablecellscope
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestTablecellverticalalignViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestTablecellverticalalignViewSet, self).setUp()
        self.url_list = reverse('valuesets:TableCellVerticalAlign-list')
        self.url_detail = 'valuesets:TableCellVerticalAlign-detail'
        self.model = Tablecellverticalalign
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestTableframeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestTableframeViewSet, self).setUp()
        self.url_list = reverse('valuesets:TableFrame-list')
        self.url_detail = 'valuesets:TableFrame-detail'
        self.model = Tableframe
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestTablerulesViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestTablerulesViewSet, self).setUp()
        self.url_list = reverse('valuesets:TableRules-list')
        self.url_detail = 'valuesets:TableRules-detail'
        self.model = Tablerules
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestTargetawarenessViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestTargetawarenessViewSet, self).setUp()
        self.url_list = reverse('valuesets:TargetAwareness-list')
        self.url_detail = 'valuesets:TargetAwareness-detail'
        self.model = Targetawareness
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestTelecommunicationcapabilitiesViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestTelecommunicationcapabilitiesViewSet, self).setUp()
        self.url_list = reverse('valuesets:TelecommunicationCapabilities-list')
        self.url_detail = 'valuesets:TelecommunicationCapabilities-detail'
        self.model = Telecommunicationcapabilities
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestTimingeventViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestTimingeventViewSet, self).setUp()
        self.url_list = reverse('valuesets:TimingEvent-list')
        self.url_detail = 'valuesets:TimingEvent-detail'
        self.model = Timingevent
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestTransmissionrelationshiptypecodeViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestTransmissionrelationshiptypecodeViewSet, self).setUp()
        self.url_list = reverse(
            'valuesets:TransmissionRelationshipTypeCode-list')
        self.url_detail = 'valuesets:TransmissionRelationshipTypeCode-detail'
        self.model = Transmissionrelationshiptypecode
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestTribalentityusViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestTribalentityusViewSet, self).setUp()
        self.url_list = reverse('valuesets:TribalEntityUS-list')
        self.url_detail = 'valuesets:TribalEntityUS-detail'
        self.model = Tribalentityus
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestVaccinemanufacturerViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestVaccinemanufacturerViewSet, self).setUp()
        self.url_list = reverse('valuesets:VaccineManufacturer-list')
        self.url_detail = 'valuesets:VaccineManufacturer-detail'
        self.model = Vaccinemanufacturer
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestHl7realmViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestHl7realmViewSet, self).setUp()
        self.url_list = reverse('valuesets:hl7Realm-list')
        self.url_detail = 'valuesets:hl7Realm-detail'
        self.model = Hl7realm
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestHl7v3conformanceViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestHl7v3conformanceViewSet, self).setUp()
        self.url_list = reverse('valuesets:hl7V3Conformance-list')
        self.url_detail = 'valuesets:hl7V3Conformance-detail'
        self.model = Hl7v3conformance
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestOrderabledrugformViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestOrderabledrugformViewSet, self).setUp()
        self.url_list = reverse('valuesets:orderableDrugForm-list')
        self.url_detail = 'valuesets:orderableDrugForm-detail'
        self.model = Orderabledrugform
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'


class TestSubstanceadminsubstitutionViewSet(APITestCase, BaseViewsTest):
    def setUp(self):
        super(TestSubstanceadminsubstitutionViewSet, self).setUp()
        self.url_list = reverse('valuesets:substanceAdminSubstitution-list')
        self.url_detail = 'valuesets:substanceAdminSubstitution-detail'
        self.model = Substanceadminsubstitution
        self.code = 'code0'
        self.code1 = 'code1'
        self.code2 = 'code2'
