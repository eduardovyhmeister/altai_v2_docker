var surveyJSON = {
    "title": "Accessibility and universal design",
    "completedHtml": "Thanks for completing this section",
    "pages": [
        {
            "name": "page1",
            "elements": [
                {
                    "type": "radiogroup",
                    "name": "DNFQ2.1-B",
                    "title": "DNF-Q2.1 Did you ensure that the AI system corresponds to the variety of preferences and abilities in the society?",
                    "isRequired": true,
                    "choices": [
                        "Yes", "No"
                    ]
                }, {
                    "type": "comment",
                    "name": "DNFQ2.1Yes-B",
                    "visibleIf": "{DNFQ2.1-B} = 'Yes'",
                    "title": "If yes, please explain:"
                }, {
                    "type": "radiogroup",
                    "name": "DNFQ2.2-B",
                    "title": "DNFQ2.2 Did you assess that the UI (user interface) of the AI system is usable by those with special needs or disabilities or those at risk of exclusion?",
                    "isRequired": true,
                    "choices": [
                        "Yes", "No"
                    ]
                }, {
                    "type": "radiogroup",
                    "name": "DNFQ2.3-B",
                    "title": "DNFQ2.3 Did you ensure that information about, and the UI of, the AI system is accessible and usable also to users of assistive technologies (such as screenreaders)?",
                    "isRequired": true,
                    "choices": [
                        "Yes", "No"
                    ]
                }, {
                    "type": "radiogroup",
                    "name": "DNFQ2.4-B",
                    "title": "DNFQ2.4 Did you involve or consult with users in need for assistive technology during the planning and development phase of the AI system?",
                    "isRequired": true,
                    "choices": [
                        "Yes", "No"
                    ]
                }, {
                    "type": "radiogroup",
                    "name": "DNFQ2.5-B",
                    "title": "DNFQ2.5 Did you ensure that Universal Design principles are taken into account during every step of the planning and development process, if applicable?",
                    "isRequired": true,
                    "choices": [
                        "Yes", "No"
                    ]
                }, {
                    "type": "radiogroup",
                    "name": "DNFQ2.6-B",
                    "title": "DNFQ2.6 Did you put in place accessible verification methods and documentation to measure and ensure different aspects of the system's reliability and reproducibility?",
                    "isRequired": true,
                    "choices": [
                        "Yes", "No"
                    ]
                }, {
                   "type": "radiogroup",
                   "name": "DNFQ2.7-B",
                   "title": "DNFQ2.7 Did you take the impact of your AI system on the potential user audience into account?",
                   "isRequired": true,
                   "choices": [
                       "Yes", "No"
                   ]
               }, {
                   "type": "radiogroup",
                   "name": "DNFQ2.8-B",
                   "title": "DNFQ2.8 Did you assess whether the team involved in building the AI system is representative of the possible target user audiences?",
                   "isRequired": true,
                   "choices": [
                       "Yes", "No"
                   ]
               }, {
                   "type": "radiogroup",
                   "name": "DNFQ2.9-B",
                   "title": "DNFQ2.9 Did you assess whether there could be groups who might be disproportionately affected by the outcomes of the system?",
                   "isRequired": true,
                   "choices": [
                       "Yes", "No"
                   ]
               }, {
                   "type": "comment",
                   "name": "DNFQ2.9Yes-B",
                    "visibleIf": "{DNFQ2.9-B} = 'Yes'",
                   "title": "If yes, please explain:",
               }, {
                   "type": "radiogroup",
                   "name": "DNFQ2.10-B",
                   "title": "DNFQ2.10 Did you assess the risk of the possible unfairness of the system onto the target user communities?",
                   "isRequired": true,
                   "choices": [
                       "Yes", "No"
                   ]
               }, {
                   "type": "comment",
                   "name": "DNFQ2.10Yes-B",
                    "visibleIf": "{DNFQ2.10-B} = 'Yes'",
                   "title": "If yes, please explain:",
               }, {
                    "type": "radiogroup",
                    "name": "DNFS2-R",
                    "title": "Based on your answers to the previous questions, how would you rate the measures you implemented to ensure accessibility and Universal Design?",
                    "isRequired": true,
                    "choices": [
                        "Inadequate", "Sufficient", "Fully adequate"
                    ]
                },
            ]
        }
    ],
    "showQuestionNumbers": "off"
};
