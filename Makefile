SHELL := /bin/bash

help:
	ls -d

.PHONY: aerospike
aerospike:
	ansible-playbook aerospike/ansible/setup.yml

ch: clickhouse

.PHONY: clickhouse
clickhouse:
	ansible-playbook clickhouse/ansible/setup.yml

.PHONY: cockroachdb
cockroachdb:
	ansible-playbook cockroachdb/ansible/setup.yml

.PHONY: consul
consul:
	ansible-playbook consul/ansible/setup.yml

.PHONY: etcd
etcd:
	ansible-playbook etcd/ansible/setup.yml

.PHONY: flink
flink:
	ansible-playbook flink/ansible/setup.yml

.PHONY: nats
nats:
	ansible-playbook nats/ansible/setup.yml

.PHONY: mq
mq: rabbitmq

.PHONY: rabbitmq
rabbitmq:
	ansible-playbook rabbitmq/ansible/setup.yml

.PHONY: kafka
kafka: redpanda

.PHONY: redpanda
redpanda:
	ansible-playbook redpanda/ansible/setup.yml

cassandra: scylla

.PHONY: scylla
scylla:
	ansible-playbook scylla/ansible/setup.yml

es: elasticsearch

.PHONY: elasticsearch
elasticsearch:
	ansible-playbook elasticsearch/ansible/setup.yml
