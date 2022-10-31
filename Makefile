SHELL := /bin/bash

help:
	ls -d

.PHONY: aerospike
aerospike:
	ansible-playbook aerospike/ansible/setup_aerospike.yml

ch: clickhouse

.PHONY: clickhouse
clickhouse:
	ansible-playbook clickhouse/ansible/setup_clickhouse.yml

.PHONY: cockroachdb
cockroachdb:
	ansible-playbook cockroachdb/ansible/setup_cockroachdb.yml

.PHONY: consul
consul:
	ansible-playbook consul/ansible/setup_consul.yml

.PHONY: etcd
etcd:
	ansible-playbook etcd/ansible/setup_etcd.yml

.PHONY: flink
flink:
	ansible-playbook flink/ansible/setup_flink.yml

.PHONY: nats
nats:
	ansible-playbook nats/ansible/setup_nats.yml

.PHONY: mq
mq: rabbitmq

.PHONY: rabbitmq
rabbitmq:
	ansible-playbook rabbitmq/ansible/setup_rabbitmq.yml

.PHONY: kafka
kafka: redpanda

.PHONY: redpanda
redpanda:
	ansible-playbook redpanda/ansible/setup_redpanda.yml

cassandra: scylla

.PHONY: scylla
scylla:
	ansible-playbook scylla/ansible/setup_scylla.yml
