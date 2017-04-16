#!/usr/bin/env python

import sys, os
import subprocess as sp

done_jobs = []

with open('jobs.txt', 'r') as f:
	lines = f.read().split('\n')
	for i in xrange(len(lines)):
		if 'Done' in lines[i]:
			done_jobs.append(lines[i]+'\n')

process = sp.Popen(['atq'], stdout=sp.PIPE)
out, error = process.communicate()
lines = out.split('\n')[:-1]
with open('jobs.txt', 'w') as f:
	for line in lines:
		job_num = line.split('\t')[0]
		bash_command = 'at -c '+job_num+' | grep DISPLAY=:0'
		process = sp.Popen(['bash','-c', bash_command], stdout=sp.PIPE)
		out, error = process.communicate()
		out_split = out.replace('\n','').split(' ')
		# out_split[-1] = out_split[-1][:-2]
		out_split[4] += ':00'
		f.write(' '.join([job_num] + out_split[3:] + ['Pending\n']))
	for job in done_jobs:
		f.write(job)
