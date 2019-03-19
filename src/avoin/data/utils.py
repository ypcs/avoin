# -*- coding: utf-8 -*-
import os
import json
import csv
import codecs

DEFAULT_ENCODING = 'utf-8'


def open(filename, mode):
	filehandle = codecs.open(filename, mode, DEFAULT_ENCODING)
	return filehandle


def read(filename):
	return open(filename, 'r').read()


def write(filename, content):
	with open(filename, 'w') as filehandle:
		filehandle.write(content)
	return True


def add_unique_to_list(item, uniq_list):
	'''Add only unique items to list
	>>> from utils import add_unique_to_list
	>>> test_list = []
	>>> add_unique_to_list('test1', test_list)
	True
	>>> add_unique_to_list('test1', test_list)
	False
	>>> add_unique_to_list('test2', test_list)
	True
	>>> add_unique_to_list('test2', test_list)
	False
	>>> add_unique_to_list('test1', test_list)
	False
	>>> add_unique_to_list('test3', test_list)
	True
	'''
	if item in uniq_list:
		return False
	uniq_list.append(item)
	return True


def _dict_to_csv(items):
	raise NotImplementedError
	
	# TODO: Handle 3D lists etc.

	headers = []

	# Expand headers w/ dict keys
	for i in items:
		add_unique_to_list(i, headers)


def _dict_to_json(items):
	return json.dumps(items)


def _dict_to_sql(items):
	pass


def _json_to_dict(content):
	return json.loads(content)


def _csv_to_dict(content):
	raise NotImplementedError


def json_to_csv(content):
	raise NotImplementedError


def csv_to_json(content):
	raise NotImplementedError


def json_to_sql(content):
	raise NotImplementedError
