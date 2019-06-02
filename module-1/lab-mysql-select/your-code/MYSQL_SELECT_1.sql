USE PUBLICATIONS;

SELECT authors.au_id,authors.au_lname,authors.au_fname, titles.title,  publishers.pub_name
FROM authors
INNER JOIN titleauthor ON authors.au_id = titleauthor.au_id
INNER JOIN titles ON titles.title_id = titleauthor.title_id
INNER join publishers on titles.pub_id = publishers.pub_id;


SELECT a.au_id, a.au_lname, a.au_fname, p.pub_name, count(p.pub_id) as title_count
FROM authors a
INNER JOIN TITLEAUTHOR T ON A.AU_ID = T.AU_ID
INNER JOIN TITLES TI ON T.TITLE_ID = TI.TITLE_ID
INNER JOIN PUBLISHERS P ON TI.PUB_ID = P.PUB_ID
group by au_id, p.pub_name
order by au_id desc;

SELECT a.au_id, a.au_lname, a.au_fname,  sum(ti.ytd_sales) as total 
from authors a
INNER JOIN TITLEAUTHOR T ON A.AU_ID = T.AU_ID
INNER JOIN TITLES TI ON T.TITLE_ID = TI.TITLE_ID
group by a.au_id
order by total desc limit 3;

SELECT a.au_id, a.au_lname, a.au_fname,  sum(ti.ytd_sales) as total 
from authors a
INNER JOIN TITLEAUTHOR T ON A.AU_ID = T.AU_ID
INNER JOIN TITLES TI ON T.TITLE_ID = TI.TITLE_ID
group by a.au_id
order by total desc ;

#update titles set price  = 0 where price  is null;





#Error Code: 1054. Unknown column 'titles.title' in 'field list'
#titles.pub_id, publishers.pub_name, publishers.pub_id,
#Error Code: 1055. Expression #1 of SELECT list is not in GROUP BY 
#clause and contains nonaggregated column 'publications.authors.au_id' 
#which is not functionally dependent on columns in GROUP BY clause; this is 
#incompatible with sql_mode=only_full_group_by
