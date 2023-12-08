from kafka.admin import KafkaAdminClient, NewTopic

admin_client = KafkaAdminClient(bootstrap_servers=['localhost:9093'])
new_topic = NewTopic(name='userportfolio',
                     num_partitions=2,
                     replication_factor=1)
admin_client.create_topics(new_topics=[new_topic])

admin_client = KafkaAdminClient(bootstrap_servers=['localhost:9093'])
new_topic = NewTopic(name='rates',
                     num_partitions=2,
                     replication_factor=1)
admin_client.create_topics(new_topics=[new_topic])


admin_client = KafkaAdminClient(bootstrap_servers=['localhost:9092'])
new_topic = NewTopic(name='fraud',
                     num_partitions=3,
                     replication_factor=2)
admin_client.create_topics(new_topics=[new_topic])


admin_client = KafkaAdminClient(bootstrap_servers=['localhost:9094'])
new_topic = NewTopic(name='tax',
                     num_partitions=5,
                     replication_factor=3)
admin_client.create_topics(new_topics=[new_topic])
