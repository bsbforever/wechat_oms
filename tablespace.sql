select a.tablespace_name,a.bytes/1024/ 1024 "Sum MB",(a.bytes-b.bytes)/1024 /1024 "used MB"
,b.bytes/ 1024/1024 "free MB",round(((a.bytes-b.bytes)/a.bytes)*100 ,2
) "percent_used"
from
(select tablespace_name, sum(bytes) bytes from dba_data_files group by tablespace_name) a,
(select tablespace_name, sum(bytes) bytes,max (bytes) largest from dba_free_space
 group by tablespace_name) b
where a.tablespace_name=b.tablespace_name
