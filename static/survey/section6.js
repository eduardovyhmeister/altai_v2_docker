var surveyJSON = {
    "title": "Stakeholder participation",
    "completedHtml": "Thanks for completing this section",
    "pages": [
        {
            "name": "page1",
            "elements": [
                {
                    "type": "radiogroup",
                    "name": "DNFQ3.1-B",
                    "title": "DNF-Q3.1 Did you consider a mechanism to include the participation of the widest range of possible stakeholders in the AI system’s design and development?",
                    "isRequired": true,
                    "choices": [
                        "Yes", "No"
                    ]
                }, {
                    "type": "comment",
                    "name": "DNFQ3.1Yes-B",
                    "visibleIf": "{DNFQ3.1} = 'Yes'",
                    "title": "If yes, please explain:"
                }, {
                    "type": "radiogroup",
                    "name": "DNFQ3.2-B",
                    "title": "DNFQ3.2 If applicable, did you pave the way for the introduction of the AI system in your organisation by informing and consulting with impacted workers and their representatives in advance?",
                    "isRequired": true,
                    "choices": [
                        "Yes", "No"
                    ]
                }, {
                    "type": "radiogroup",
                    "name": "DNFS3-R",
                    "title": "Based on your answers to the previous questions, how would you rate the measures you put in place to ensure the involvement of the relevant stakeholders?",
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
