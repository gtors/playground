help:
	ls -d

aerospike:
	ansible-playbook aerospike/ansible/setup.yml

ch: clickhouse

clickhouse:
	ansible-playbook clickhouse/ansible/setup.yml

cockroachdb:
	ansible-playbook cockroachdb/ansible/setup.yml

consul:
	ansible-playbook consul/ansible/setup.yml

etcd:
	ansible-playbook etcd/ansible/setup.yml

flink:
	ansible-playbook flink/ansible/setup.yml

nats:
	ansible-playbook nats/ansible/setup.yml

mq: rabbitmq

rabbitmq:
	ansible-playbook rabbitmq/ansible/setup.yml

kafka: redpanda

redpanda:
	ansible-playbook redpanda/ansible/setup.yml

cassandra: scylla

scylla:
	ansible-playbook scylla/ansible/setup.yml

es: elasticsearch

elasticsearch:
	ansible-playbook elasticsearch/ansible/setup.yml

chronogaf:
	ansible-playbook chronograf/ansible/setup.yml
