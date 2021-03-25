{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "········\n",
      "environment set\n"
     ]
    }
   ],
   "source": [
    "\n",
    "import pyodbc\n",
    "from getpass import getpass\n",
    "from subprocess import Popen, PIPE\n",
    "import subprocess\n",
    "\n",
    "\n",
    "def set_env(conn, queue):\n",
    "    \"\"\"Sets the hive execution engine and the queue that we wish to use\"\"\"    \n",
    "    cursor = conn.cursor()\n",
    "    cursor.execute(\"SET hive.execution.engine = tez;\")\n",
    "    cursor.execute(\"SET hive.groupby.orderby.position.alias = true;\")\n",
    "    cursor.execute(\"SET hive.resultset.use.unique.column.names = false;\")\n",
    "    cursor.execute(\"SET hive.auto.convert.join = true;\")\n",
    "    print(\"environment set\")  \n",
    "\n",
    "def get_conn(userid):\n",
    "    \"\"\"Returns ODBC connection to dox\"\"\"    \n",
    "    kinit_args = [ 'kinit', '%s@UK.CENTRICAPLC.COM' % (userid) ]\n",
    "    kinit = subprocess.Popen(kinit_args, stdin=PIPE, stdout=PIPE, stderr=PIPE)\n",
    "    kinit.stdin.write(getpass().encode(\"utf-8\"))\n",
    "    kinit.stdin.close()\n",
    "    conn =pyodbc.connect(\"DSN=doxhttphive\", autocommit=True)\n",
    "    set_env(conn,'')\n",
    "    return(conn)\n",
    "    print(\"connection successful\")\n",
    "    \n",
    "userid=\"nurmohas\"\n",
    "conn=get_conn(userid)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "ename": "DatabaseError",
     "evalue": "Execution failed on sql ' \nSELECT * FROM data_science.ars_nat_54u8_deep_dive2_ds\nLIMIT 100;\n': ('42S02', '[42S02] [Hortonworks][SQLEngine] (31740) Table or view not found: HIVE.data_science.ars_nat_54u8_deep_dive2_ds (31740) (SQLExecDirectW)')",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mProgrammingError\u001b[0m                          Traceback (most recent call last)",
      "\u001b[0;32m/software/microsoft/mlserver/9.3.0/runtime/python/lib/python3.5/site-packages/pandas/io/sql.py\u001b[0m in \u001b[0;36mexecute\u001b[0;34m(self, *args, **kwargs)\u001b[0m\n\u001b[1;32m   1430\u001b[0m             \u001b[0;32melse\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m-> 1431\u001b[0;31m                 \u001b[0mcur\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mexecute\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m*\u001b[0m\u001b[0margs\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m   1432\u001b[0m             \u001b[0;32mreturn\u001b[0m \u001b[0mcur\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;31mProgrammingError\u001b[0m: ('42S02', '[42S02] [Hortonworks][SQLEngine] (31740) Table or view not found: HIVE.data_science.ars_nat_54u8_deep_dive2_ds (31740) (SQLExecDirectW)')",
      "\nDuring handling of the above exception, another exception occurred:\n",
      "\u001b[0;31mDatabaseError\u001b[0m                             Traceback (most recent call last)",
      "\u001b[0;32m<ipython-input-2-dc5a2f738370>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m()\u001b[0m\n\u001b[1;32m      4\u001b[0m \"\"\"\n\u001b[1;32m      5\u001b[0m \u001b[0;31m#data_science.dt_parts_ndc_national\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 6\u001b[0;31m \u001b[0mpath2\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mpd\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mread_sql\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mmy_sql\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mconn\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[0;32m/software/microsoft/mlserver/9.3.0/runtime/python/lib/python3.5/site-packages/pandas/io/sql.py\u001b[0m in \u001b[0;36mread_sql\u001b[0;34m(sql, con, index_col, coerce_float, params, parse_dates, columns, chunksize)\u001b[0m\n\u001b[1;32m    378\u001b[0m             \u001b[0msql\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mindex_col\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mindex_col\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mparams\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mparams\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    379\u001b[0m             \u001b[0mcoerce_float\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mcoerce_float\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mparse_dates\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mparse_dates\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 380\u001b[0;31m             chunksize=chunksize)\n\u001b[0m\u001b[1;32m    381\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    382\u001b[0m     \u001b[0;32mtry\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m/software/microsoft/mlserver/9.3.0/runtime/python/lib/python3.5/site-packages/pandas/io/sql.py\u001b[0m in \u001b[0;36mread_query\u001b[0;34m(self, sql, index_col, coerce_float, params, parse_dates, chunksize)\u001b[0m\n\u001b[1;32m   1466\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   1467\u001b[0m         \u001b[0margs\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0m_convert_params\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0msql\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mparams\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m-> 1468\u001b[0;31m         \u001b[0mcursor\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mexecute\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m*\u001b[0m\u001b[0margs\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m   1469\u001b[0m         \u001b[0mcolumns\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;34m[\u001b[0m\u001b[0mcol_desc\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;36m0\u001b[0m\u001b[0;34m]\u001b[0m \u001b[0;32mfor\u001b[0m \u001b[0mcol_desc\u001b[0m \u001b[0;32min\u001b[0m \u001b[0mcursor\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mdescription\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   1470\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m/software/microsoft/mlserver/9.3.0/runtime/python/lib/python3.5/site-packages/pandas/io/sql.py\u001b[0m in \u001b[0;36mexecute\u001b[0;34m(self, *args, **kwargs)\u001b[0m\n\u001b[1;32m   1443\u001b[0m                 \"Execution failed on sql '{sql}': {exc}\".format(\n\u001b[1;32m   1444\u001b[0m                     sql=args[0], exc=exc))\n\u001b[0;32m-> 1445\u001b[0;31m             \u001b[0mraise_with_traceback\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mex\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m   1446\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   1447\u001b[0m     \u001b[0;34m@\u001b[0m\u001b[0mstaticmethod\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m/software/microsoft/mlserver/9.3.0/runtime/python/lib/python3.5/site-packages/pandas/compat/__init__.py\u001b[0m in \u001b[0;36mraise_with_traceback\u001b[0;34m(exc, traceback)\u001b[0m\n\u001b[1;32m    418\u001b[0m         \u001b[0;32mif\u001b[0m \u001b[0mtraceback\u001b[0m \u001b[0;34m==\u001b[0m \u001b[0mEllipsis\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    419\u001b[0m             \u001b[0m_\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0m_\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mtraceback\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0msys\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mexc_info\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 420\u001b[0;31m         \u001b[0;32mraise\u001b[0m \u001b[0mexc\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mwith_traceback\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mtraceback\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    421\u001b[0m \u001b[0;32melse\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    422\u001b[0m     \u001b[0;31m# this version of raise is a syntax error in Python 3\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m/software/microsoft/mlserver/9.3.0/runtime/python/lib/python3.5/site-packages/pandas/io/sql.py\u001b[0m in \u001b[0;36mexecute\u001b[0;34m(self, *args, **kwargs)\u001b[0m\n\u001b[1;32m   1429\u001b[0m                 \u001b[0mcur\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mexecute\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m*\u001b[0m\u001b[0margs\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m**\u001b[0m\u001b[0mkwargs\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   1430\u001b[0m             \u001b[0;32melse\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m-> 1431\u001b[0;31m                 \u001b[0mcur\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mexecute\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m*\u001b[0m\u001b[0margs\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m   1432\u001b[0m             \u001b[0;32mreturn\u001b[0m \u001b[0mcur\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   1433\u001b[0m         \u001b[0;32mexcept\u001b[0m \u001b[0mException\u001b[0m \u001b[0;32mas\u001b[0m \u001b[0mexc\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;31mDatabaseError\u001b[0m: Execution failed on sql ' \nSELECT * FROM data_science.ars_nat_54u8_deep_dive2_ds\nLIMIT 100;\n': ('42S02', '[42S02] [Hortonworks][SQLEngine] (31740) Table or view not found: HIVE.data_science.ars_nat_54u8_deep_dive2_ds (31740) (SQLExecDirectW)')"
     ]
    }
   ],
   "source": [
    "my_sql = \"\"\" \n",
    "SELECT * FROM data_science.ars_nat_54u8_deep_dive2_ds\n",
    "LIMIT 100;\n",
    "\"\"\"\n",
    "#data_science.dt_parts_ndc_national\n",
    "path2 = pd.read_sql(my_sql, conn)  "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "path2.sample(5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "pd.set_option('display.max_columns', 500)\n",
    "import numpy as np\n",
    "from scipy import stats\n",
    "import seaborn as sb\n",
    "import matplotlib.pyplot as plt\n",
    "%matplotlib inline"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "ename": "ImportError",
     "evalue": "No module named 'lifelines'",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mImportError\u001b[0m                               Traceback (most recent call last)",
      "\u001b[0;32m<ipython-input-2-91160498a4a1>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m()\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0;32mfrom\u001b[0m \u001b[0mlifelines\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mplotting\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mplot_lifetimes\u001b[0m      \u001b[0;31m# Lifeline package for the Survival Analysis\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      2\u001b[0m \u001b[0mget_ipython\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mmagic\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m'pylab inline'\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      3\u001b[0m \u001b[0mfigsize\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;36m12\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;36m6\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;31mImportError\u001b[0m: No module named 'lifelines'"
     ]
    }
   ],
   "source": [
    "from lifelines.plotting import plot_lifetimes      # Lifeline package for the Survival Analysis\n",
    "%pylab inline\n",
    "figsize(12,6)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "#Ficticious data\n",
    "\n",
    "from lifelines import KaplanMeierFitter\n",
    "\n",
    "## Example Data \n",
    "durations = [5,6,6,2.5,4,4]\n",
    "event_observed = [1, 0, 0, 1, 1, 1]\n",
    "\n",
    "## create an kmf object\n",
    "kmf = KaplanMeierFitter() \n",
    "\n",
    "## Fit the data into the model\n",
    "kmf.fit(durations, event_observed,label='Kaplan Meier Estimate')\n",
    "\n",
    "## Create an estimate\n",
    "kmf.plot(ci_show=False) ## ci_show is meant for Confidence interval, since our data set is too tiny, thus i am not showing it."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "###Real World Example"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "##  create a dataframe\n",
    "df = pd.read_csv(\"Telco_Customer_Churn.csv\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "## Have a first look at the data\n",
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "## Data Types and Missing Values in Columns\n",
    "df.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "## Convert TotalCharges to numeric\n",
    "df['TotalCharges']=pd.to_numeric(df['TotalCharges'],errors='coerce')\n",
    "\n",
    "## Replace yes and No in the Churn column to 1 and 0. 1 for the event and 0 for the censured data.\n",
    "df['Churn']=df['Churn'].apply(lambda x: 1 if x == 'Yes' else 0 )"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "## after converting the column TotalCharges to numeric\n",
    "df.info()  ## Column TotalCharges is having missing values"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "## Impute the null value with the median value\n",
    "\n",
    "df.TotalCharges.fillna(value=df['TotalCharges'].median(),inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "## Create a list of Categorical Columns\n",
    "cat_cols= [i  for i in df.columns if df[i].dtype==object]\n",
    "cat_cols.remove('customerID')  ## customerID has been removed because it is unique for all the rows."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "## lets have a look at the categories and their distribution in all the categorical columns.\n",
    "\n",
    "for i in cat_cols:\n",
    "    print('Column Name: ',i)\n",
    "    print(df[i].value_counts())\n",
    "    print('-----------------------------')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "## Lets create an overall KaplanMeier curve, without breaking it into groups of covariates.\n",
    "## Import the library\n",
    "from lifelines import KaplanMeierFitter\n",
    "\n",
    "\n",
    "durations = df['tenure'] ## Time to event data of censored and event data\n",
    "event_observed = df['Churn']  ## It has the churned (1) and censored is (0)\n",
    "\n",
    "## create a kmf object as km\n",
    "km = KaplanMeierFitter() ## instantiate the class to create an object\n",
    "\n",
    "## Fit the data into the model\n",
    "km.fit(durations, event_observed,label='Kaplan Meier Estimate')\n",
    "\n",
    "## Create an estimate\n",
    "km.plot()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "## Lets create Kaplan Meier Curves for Cohorts\n",
    "kmf = KaplanMeierFitter() \n",
    "\n",
    "\n",
    "T = df['tenure']     ## time to event\n",
    "E = df['Churn']      ## event occurred or censored\n",
    "\n",
    "\n",
    "groups = df['Contract']             ## Create the cohorts from the 'Contract' column\n",
    "ix1 = (groups == 'Month-to-month')   ## Cohort 1\n",
    "ix2 = (groups == 'Two year')         ## Cohort 2\n",
    "ix3 = (groups == 'One year')         ## Cohort 3\n",
    "\n",
    "\n",
    "kmf.fit(T[ix1], E[ix1], label='Month-to-month')    ## fit the cohort 1 data\n",
    "ax = kmf.plot()\n",
    "\n",
    "\n",
    "kmf.fit(T[ix2], E[ix2], label='Two year')         ## fit the cohort 2 data\n",
    "ax1 = kmf.plot(ax=ax)\n",
    "\n",
    "\n",
    "kmf.fit(T[ix3], E[ix3], label='One year')        ## fit the cohort 3 data\n",
    "kmf.plot(ax=ax1)                                 ## Plot the KM curve for three cohort on same x and y axis"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "kmf1 = KaplanMeierFitter() ## instantiate the class to create an object\n",
    "\n",
    "## Two Cohorts are compared. 1. Streaming TV Not Subsribed by Users, 2. Streaming TV subscribed by the users.\n",
    "groups = df['StreamingTV']   \n",
    "i1 = (groups == 'No')      ## group i1 , having the pandas series for the 1st cohort\n",
    "i2 = (groups == 'Yes')     ## group i2 , having the pandas series for the 2nd cohort\n",
    "\n",
    "\n",
    "## fit the model for 1st cohort\n",
    "kmf1.fit(T[i1], E[i1], label='Not Subscribed StreamingTV')\n",
    "a1 = kmf1.plot()\n",
    "\n",
    "## fit the model for 2nd cohort\n",
    "kmf1.fit(T[i2], E[i2], label='Subscribed StreamingTV')\n",
    "kmf1.plot(ax=a1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "##COX PROPOTIONAL HAZARD MODEL (Survival Regression)\n",
    "from lifelines import CoxPHFitter"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "# My objective here is to introduce you to the implementation of the model.Thus taking subset of the columns to train the model.\n",
    "## Only using the subset of the columns present in the original data\n",
    "df_r= df.loc[:,['tenure','Churn','gender','Partner','Dependents','PhoneService','MonthlyCharges','SeniorCitizen','StreamingTV']]\n",
    "df_r.head() ## have a look at the data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "## Create dummy variables\n",
    "df_dummy = pd.get_dummies(df_r, drop_first=True)\n",
    "df_dummy.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "# Using Cox Proportional Hazards model\n",
    "cph = CoxPHFitter()   ## Instantiate the class to create a cph object\n",
    "cph.fit(df_dummy, 'tenure', event_col='Churn')   ## Fit the data to train the model\n",
    "cph.print_summary()    ## Have a look at the significance of the features"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "cph.plot()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "## Check all the methods and attributes associated with the cph object.\n",
    "dir(cph)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "## We want to see the Survival curve at the customer level. Therefore, we have selected 6 customers (rows 5 till 9).\n",
    "tr_rows = df_dummy.iloc[5:10, 2:]\n",
    "tr_rows"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "## Lets predict the survival curve for the selected customers. \n",
    "## Customers can be identified with the help of the number mentioned against each curve.\n",
    "cph.predict_survival_function(tr_rows).plot()"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "MLSPython",
   "language": "python",
   "name": "mlspython"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.5.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 1
}
