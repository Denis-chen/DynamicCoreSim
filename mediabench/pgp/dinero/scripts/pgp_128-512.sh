#!/opt/local/bin/tcsh -f
# Script for the simulation
#
# the location of benchmark
set path = ../bin
set dpath = ../data
#benchmark name
set benchmark1 = pgpencode
set benchmark2 = pgpdecode
set data1 = pgptest.plain
set data2 = pgptest.enc
set out = 
#benchmark options
set options1 = "-es"
set options2 = "-db"
set input1 = "${dpath}/${data1}"
set input2 = "${dpath}/${data2}.pgp"
set output1 = "Bill -zbillms -u Bill"
set output2 = "-zbillms"
set args1 = "${options1} ${input1} ${output1}"
set args2 = "${options2} ${input2} ${output2}"
#
#deletions
# After encruption: ${data1}.pgp
# After decryption: ${data2}, ${data2}.sig
set count = 2000000000
set cache = 128
set line = 16
set assoc = 1
set upper = 1000
#
set analyzer = /u/gs3/leec/leec/Projects/shade/bin/gen
set dinero = /u/class/cs251a/dinero/dineroIII
set rm = /usr/bin/rm
#
while ( ${cache} < ${upper} )
${analyzer} -o ${benchmark1}.${cache}.summary -- ${path}/${benchmark1} ${args1} | ${dinero} -b${line} -d${cache} -i${cache} -a${assoc} -z${count} > ${benchmark1}.${cache}.dinero
# cleanup
${rm} -f ${dpath}/${data1}.pgp
#
${analyzer} -o ${benchmark2}.${cache}.summary -- ${path}/${benchmark2} ${args2} | ${dinero} -b${line} -d${cache} -i${cache} -a${assoc} -z${count} > ${benchmark2}.${cache}.dinero
# cleanup
${rm} -f ${dpath}/${data2} ${dpath}/${data2}.sig
#
 @ cache = ${cache} * 2
end
