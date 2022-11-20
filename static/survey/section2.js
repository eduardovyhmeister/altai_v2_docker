
var surveyJSON = {  
    "title": "Technical Robustness and Safety", 
    "completedHtml": "Thanks for completing this section",
    "pages": [
        {
            "name": "page1",
            "elements": [
                {
                    "type": "radiogroup",
                    "name": "HAO1",
                    "title": "HAO1 - This is a placeholder for the icons? [![Comment](/img/icons/blog.svg =18x18)](/QuestionFeedback?questionId=HAO1)  [![Info](/img/icons/info.svg =18x18)](https://ec.europa.eu/futurium/en/ai-alliance-consultation)",
                    "isRequired": true,
                    "choices": [
                        "No", "To some extent", "Yes", "I dont know"
                    ]
                }, {
                    "type": "comment",
                    "name": "HAO1C",

                    "visibleIf": "{HAO1} = 'I dont know'",
                    "title": "Check the definition of Human Agency in Chapter 2 of the guidelines and come back. If the question is still not clear pls provide a feedback"
                }, {
                    "type": "radiogroup",
                    "name": "HAO1.1",
                    "visibleIf": "{HAO1} = 'No' or {HAO1} = 'To some extent'",
                    "title": "HAO1.1 Could the AI system generate confusion for some or all users on whether they are interacting with a human or a non-human agent? ![A cat](https://surveyjs.io/Content/Images/examples/markdown/cat.svg =14x14)",
                    "isRequired": true,
                    "choices": [
                        "Yes", "No"
                    ]
                }, {
                    "type": "radiogroup",
                    "name": "HAOQ1",
                    "visibleIf": "{HAO1.1} = 'Yes'",
                    "title": "HAO-Q1 Are the human end users informedthat they are interacting with a non-human agent?  ![Comment](/img/icons/blog.svg =18x18)",
                    "isRequired": true,
                    "choices": [
                        "Yes", "No"
                    ]
                }, {
                    "type": "radiogroup",
                    "name": "HAO1.2",
                    "title": "HA01.2 Could the AI system generate confusion for some or all users on whether a decision, content, advice or outcome is the result of an algorithmic decision? ",
                    "isRequired": true,
                    "choices": [
                        "Yes", "No"
                    ]
                }, {
                    "type": "radiogroup",
                    "name": "HAO-Q2",
                    "visibleIf": "{HAO1.2} == 'Yes'",
                    "title": "HAO-Q2  Are  the  human  end  users  made  adequately  aware  that  the  decision,  content,  advice  or outcome is the result of an algorithmic decision?",
                    "isRequired": true,
                    "choices": [
                        "Yes", "No"
                    ]
                }, {
                    "type": "radiogroup",
                    "name": "HAO1.3",
                    "visibleIf": "{HAO1.2} == 'Yes'",

                    "title": "HAO1.3 Could the AI system affect human autonomy by generating over-reliance by users?",
                    "isRequired": true,
                    "choices": [
                        "No", "To some extent", "Yes", "I dont know"
                    ]
                }, {
                    "type": "html",
                    "name": "HAO1.3Video",
                    "visibleIf": "{HAO1.3} = 'I dont know'",
                    "html": "Here we show a video: Unintended ways"
                }, {
                    "type": "radiogroup",
                    "name": "HAOQ3",
                    "visibleIf": "{HAO1.3} = 'Yes' or {HAO1.3} = 'To some extent'",
                    "title": "HAOQ3 Have you put in place procedures to avoid that users over-rely on the AI system?",
                    "isRequired": true,
                    "choices": [
                        "Yes", "No"
                    ]
                }, {
                    "type": "comment",
                    "name": "HAOQ3-Yes",
                    "visibleIf": "{HAOQ3} = 'Yes'",
                    "title": "Please explain the procedures"
                },
            ]
        }
    ],
    "showQuestionNumbers": "off"
};
