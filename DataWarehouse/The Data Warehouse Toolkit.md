# The Data Warehouse Toolkit

---

## Table of contents
1. [Chapter 1 DW/BI & Dimentional Modeling](#chapter1)
	1. [Goal of DW/BI](#goal)
	2. [DW/BI manager's responsibilities](#responsibility)
	3. [Dimentional Modeling Introduction](#dimension-intro)
	4. [Star Scheams vs. OLAP](#compare)
	5. [Kimball's DW/BI Architecture](#kimball)
	6. [Alternative DW/BI Architectures](#alternative)
2. [Charpter 2]

---

## Chapter 1: Data Warehousing Business Intelligence and Dimensional Modeling Prier <a name="chapter1"></a>

**Operational system**: where you put the data in <br/>
**DW/BI system**: where you get the data out

### Goals of DW/BI <a name="goal"></a>

- Make info easily accessible: understandable, simple and fast
- Present info consistently
- DW/BI must adapt to change: existing data shouldn't change when new data added
- Present info in a timely way
- Deliver data when there is little time to clean or validate it
- DW/BI system must serve as the authoritative and trustworthy foundation for improved decision making
- The business community ust accept the DW/BI system to deem it successful

### DW/BI manager's responsibilities <a name="responsibility"></a>
- Understand the business users
- Deliver high-quality, relevant, and accessible information and analytics to the business users
- Sustain the DW/BI environment


### Dimentional Modeling Introduction <a name="dimension-intro"></a>
**Address two requirements:**
- Deliver data that is understandable to the business users
- Deliver fast query performance
> - "Make everything as simple as possible, but not simpler." Albert Einstein
> - 3NF: too complicated for BI queries. Users can't understand, navigate, or remember normalized models.
> - Dimensional model: address the problem of overly complex schemas in the presentation area.

### Star Scheams vs. OLAP (online analytical processing) Cubes <a name="compare"></a>

**Star shemas**
- Dimention table: "who, what, where, whhen, how, why" (usually no more than 50 attributes)
- Fact table: measurements
- Dimensions provide the entry points to the data, and the final labels and groupings on all DW/BI analysis
<img src="https://github.com/ZhijunLiu96/Notes/tree/master/DataWarehose/figure/1-1.png">

```sql
SELECT
	store.district_name,
	product.brand,
	SUM(sales_facts.sales_dollars) AS sales_dollars
FROM
	store,
	product,
	date,
	sales_facts
WHERE
	date.month_name = 'January' AND
	date.year = 2013 AND 
	store.store_key = sales_facts.store_key AND 
	product.product_key = sales_facts.product_key AND
	date.date_key = sales_fatcs.date_key
GROUP BY
	store.district_name
	product.brand
```

**OLAP**
- Data is stored and indexed using format and techniques that are designed for dimensional data
- Create performance aggregations or precalculated summary tables
- Cubes deliver suoerior query performance (b/c precalculations, indexing strategies)
<img src="https://github.com/ZhijunLiu96/Notes/tree/master/DataWarehose/figure/1-2.png">

### Kimball's DW/BI Architecture <a name="kimball"></a>
<img src="https://github.com/ZhijunLiu96/Notes/tree/master/DataWarehose/figure/1-3.png">

**ETL**
- Understand the source data
- Copy the data into ETL system
- Other potential transformations: cleanse the data, combine data from multiple sources, de-duplicate data
- Load data into the presentation area's target dimensional models

**Presentation Area (Support Business Intelligence)**
- Data should be presented, stored, and accessed in dimentional shcemas 
- The presentation area should include detailed, atomic data (for unpredictable ad hoc user queries)
- The presentation data area should be structured around business process measurement events
- All the dimensional structures must be built using common, conformed dimensions

**Business Intelligence Applications**
- All BI applications query the data in presentation are
- Such as modeling or forecasting tools


### Alternative DW/BI Architectures <a name="alternative"></a>

**Independent Data Mart Architecture**
<img src="https://github.com/ZhijunLiu96/Notes/tree/master/DataWarehose/figure/1-4.png">
- A database satisfies department's analytic requirements
- Other department don't have access
- Prevalent in large organizations
- Drawbacks: multiple uncoordinated extracts from the same operational sources, redundant storage of data
> (Difference) Dimensional Modeling: atomic details, built by business process

**Hub-and-Spoke Corporate Information Factory Inmon Architecture (CIF)**
<img src="https://github.com/ZhijunLiu96/Notes/tree/master/DataWarehose/figure/1-5.png">
- Normalized EDW (Enterprise Data Warehouse)
- Advocate enterprise data coordination and integration

**Hybrid Hub-and-Spoke and Kimball Architecture**
<img src="https://github.com/ZhijunLiu96/Notes/tree/master/DataWarehose/figure/1-6.png">

---
