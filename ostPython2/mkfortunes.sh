#!/usr/bin/bash

stmt="fortune 30% startrek 50% linuxcookie 20% fortunes2"
let count=1000
let n=1
while [ $n -le $count ]; do
	$stmt
	echo '%'
	let n=$n+1
done

