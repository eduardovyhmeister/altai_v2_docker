
var surveyJSON = {  
    "title": "Human Agency and Oversight (HAO)", 
    "processedTitle": "Human Agency and Oversight (HAO)", 
    "completedHtml": "<h3>Thank you for your feedback.</h3> <h5>Your thoughts and ideas will help us to create a great product!</h5>",
    "pages": [
        {
            "name": "page1",
            "elements": [
                {
                    "type": "html",
                    "name": "intro",
                    "html": "<iframe width=\"560\" height=\"315\" src=\"https://www.youtube.com/embed/PxpJYJiLwpc\" frameborder=\"0\" allow=\"accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture\" allowfullscreen></iframe>"
                }, {
                    "type": "radiogroup",
                    "name": "HAO1",
                    "title": "HAO1 - Is the AI system designed to interact with decisions by human (end) users (e.g. recommended actions or decisions to take; presenting options)?",
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
                    "title": "HAO1.1 Could the AI system generate confusion for some or all users on whether they are interacting with a human or a non-human agent?",
                    "isRequired": true,
                    "choices": [
                        "Yes", "No"
                    ]
                }, {
                    "type": "radiogroup",
                    "name": "HAOQ1-B",
                    "visibleIf": "{HAO1.1} = 'Yes' and ({HAO1} = 'No' or {HAO1} = 'To some extent')",
                    "title": "HAO-Q1 Are the human end users informedthat they are interacting with a non-human agent?",
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
                    "name": "HAO-Q2-B",
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
                    "name": "HAOQ3-B",
                    "visibleIf": "{HAO1.3} = 'Yes' or {HAO1.3} = 'To some extent'",
                    "title": "HAOQ3 Have you put in place procedures to avoid that users over-rely on the AI system?",
                    "isRequired": true,
                    "choices": [
                        "Yes", "No"
                    ]
                }, {
                    "type": "comment",
                    "name": "HAOQ3-Yes-B",
                    "visibleIf": "{HAOQ3} = 'Yes'",
                    "title": "Please explain the procedures"
                }, {
                    "type": "radiogroup",
                    "name": "HAO1.4",

                    "title": "HAO1.4 Could the AI system affect human autonomy by interfering with the (end) user’s decisionmaking process in any other (unintended) way?",
                    "isRequired": true,
                    "choices": [
                        "No", "To some extent", "Yes", "I dont know"
                    ]
                }, {
                    "type": "html",
                    "name": "HAO1.4Video",
                    "visibleIf": "{HAO1.4} = 'I dont know'",
                    "html": "Here we show a video: Unintended ways"
                }, {
                    "type": "radiogroup",
                    "name": "HAOQ4-B",
                    "visibleIf": "{HAO1.4} = 'Yes' or {HAO1.4} = 'To some extent'",
                    "title": "HAOQ4     Have you put in place any procedure to avoid that the system inadvertently affects human autonomy?",
                    "isRequired": true,
                    "choices": [
                        "Yes", "No"
                    ]
                }, {
                    "type": "comment",
                    "name": "HAOQ4-Yes-B",
                    "visibleIf": "{HAOQ4} = 'Yes'",
                    "title": "Please explain the procedures"
                }, {
                    "type": "radiogroup",
                    "name": "HAOS1-R",
                    "title": "HAO-S1 Based on your answers to the previous questions, how would you rate the risk that the AI system negatively affects human autonomy?   ",
                    "isRequired": true,
                    "colCount": "5",
                    "choices": [
                        "Non-existent", "Low", "Moderate", "Significant", "High"
                    ]
                }, {
                    "type": "radiogroup",
                    "name": "HAOS2-R",
                    "title": "HAO-S2.  How would you rate the measures you have adopted to mitigate this risk?",
                    "isRequired": true,
                    "choices": [
                        "Inadequate", "Sufficient ", "Fully adequate"
                    ]
                }


            ]
        }
    ],
    "showQuestionNumbers": "off"
};
