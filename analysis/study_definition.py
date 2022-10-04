from cohortextractor import StudyDefinition, patients, codelist, codelist_from_csv  # NOQA
from demographic_variables import demographic_variables


study = StudyDefinition(
    index_date="2021-01-01",
    default_expectations={
        "date": {"earliest": "1900-01-01", "latest": "today"},
        "rate": "uniform",
        "incidence": 0.5,
    },
    population=patients.satisfying(
        "complete_record AND registered",
        complete_record=patients.with_complete_gp_consultation_history_between(
            "2021-01-01", "2021-12-31"),
        registered=patients.registered_with_one_practice_between(
            "2021-01-01", "2021-12-31")
    ),
    gp_consultation_count=patients.with_gp_consultations(
        between=["index_date", "index_date + 1 month"],
        returning="number_of_matches_in_period",
        return_expectations={
            "int": {"distribution": "poisson", "mean": 3},
            "incidence": 0.25
            }
        ),
    **demographic_variables
    )

# MEASURES!?