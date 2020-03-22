import pytest

event = {'Records': [{'EventSource': 'aws:sns', 'EventVersion': '1.0',
              'EventSubscriptionArn': 'arn:aws:sns:us-east-1:811054952067:NewNEXRADLevel2Archive:92d170df-3f45-4833-b8ff-e3d7cdb8d861',
              'Sns': {'Type': 'Notification',
                      'MessageId': 'a13ce577-3c14-505c-9f47-b397c7ea8a97',
                      'TopicArn': 'arn:aws:sns:us-east-1:811054952067:NewNEXRADLevel2Archive',
                      'Subject': 'Amazon S3 Notification',
                      'Message': {"Records":[{"eventVersion":"2.1","eventSource":"aws:s3","awsRegion":"us-east-1","eventTime":"2020-03-10T02:21:39.531Z","eventName":"ObjectCreated:Put","userIdentity":{"principalId":"AWS:AROAINJPLIR64FRUFDYZO:i-0187e90c255ec4386"},"requestParameters":{"sourceIPAddress":"54.68.83.56"},"responseElements":{"x-amz-request-id":"F88B7CDC5CB60F38","x-amz-id-2":"1B+5ScF5JcdCpBMbhc874AjmQ0ru4+9+xCzgfwLBeqyN7bMjTxjQMSMOw+xoDzyLCSs3+1Y27CTdkq/N1n/adeizCPJiay57"},"s3":{"s3SchemaVersion":"1.0","configurationId":"NewNEXRADLevel2Object","bucket":{"name":"noaa-nexrad-level2","ownerIdentity":{"principalId":"A174AJZU80HRKD"},"arn":"arn:aws:s3:::noaa-nexrad-level2"},"object":{"key":"2020/03/10/KBUF/KBUF20200310_021645_V06","size":9055527,"eTag":"097940d06c46ebf6d6856d5e381a8ce6","sequencer":"005E66F9BC6F8DFE3E"}}}]},
                      'Timestamp': '2020-03-10T02:21:50.782Z',
                      'SignatureVersion': '1',
                      'Signature': 'QQVmi6kX4VhLDtUdqNz5mbLwBM44p39SdCh4G8kFlPSklBFOODg1ShqMfvWG4p7Dsqd20jrF2PePXvkKOGXMuVFIt74DMJD17PQtTar46vJkGHsyKM1DlPUl4cE/HlguXZta7XFfWmnZzbBvHSjk+86r8Ty7hyCCXlrOCQfUpu35d4n8tpaiExF07nz7g7HjFUhwe3dOokcfON3Wq+4hmwWpHsN29dQWlWASCqWyCUsaVzNcR4Re0K3IQrcquqP0KjhS5bIAQsCKR3CSaawENU/xSW+uBST6z9yjXPKAtd72NzCoPPA/Jv5708iUYvw9BBJ3o1jJY6pVOuen5rlWcg==',
                      'SigningCertUrl': 'https://sns.us-east-1.amazonaws.com/SimpleNotificationService-a86cb10b4e1f29c941702d737128f7b6.pem',
                      'UnsubscribeUrl': 'https://sns.us-east-1.amazonaws.com/?Action=Unsubscribe&SubscriptionArn=arn:aws:sns:us-east-1:811054952067:NewNEXRADLevel2Archive:92d170df-3f45-4833-b8ff-e3d7cdb8d861',
                      'MessageAttributes': {}}}]}

print(event["Records"][0]["Sns"]["Message"]["Records'''"][0]["s3"])