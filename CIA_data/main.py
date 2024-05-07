import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("c:/Users/natha/OneDrive/Desktop/GitHub Projects/CIA_data/bank.csv")
print(df.head())

print(df.shape)
df.isnull().sum()
df.describe()
df = df[df["contact"] != "unknown"]
df["contact"].value_counts()
df = df[df["poutcome"] != "unknown"]
df = df[df["poutcome"] != "other"]
df["poutcome"].value_counts()
df.head()
# Example of creating a plot
plt.figure(figsize=(15,15))
sns.countplot(x="age",data=df)
plt.show()

sns.histplot(data=df, x="age",color="navy")
plt.show()

job_counts = df['job'].value_counts()

plt.figure(figsize=(8, 8))
plt.pie(job_counts, labels=job_counts.index, autopct='%1.1f%%', startangle=140)
plt.title('Distribution of Jobs')
plt.axis('equal')  
plt.show()

df["marital"].value_counts()

sns.countplot(x="marital",data=df,palette="Set1",hue="loan")
plt.show()

ed_counts = df['education'].value_counts()

plt.figure(figsize=(8, 8))
plt.pie(ed_counts, labels=ed_counts.index, autopct='%1.1f%%', startangle=90)
plt.title('Distribution of Education')
plt.axis('equal')  
plt.show()

df["default"].value_counts()

myexplode = [0.5, 0.3]
d=df["default"].value_counts()
plt.pie(d, labels=d.index, autopct='%1.1f%%', startangle=90,explode=myexplode)
plt.show()

sns.histplot(data=df, y="balance",bins=20)
plt.show()

df.groupby(["job"])['deposit'].value_counts().unstack().plot(kind='bar',figsize=(10,5))
plt.title("Deposit by Job")
plt.xlabel("Job")
plt.ylabel("Deposit")
plt.show()

df.groupby(["job"])['marital'].value_counts().unstack().plot(kind='bar',figsize=(10,5))
plt.title("Deposit by Job")
plt.xlabel("Job")
plt.ylabel("Deposit")
plt.show()

df.groupby(["job"])['loan'].value_counts().unstack().plot(kind='bar',figsize=(10,5))
plt.title("Deposit by Job")
plt.xlabel("Job")
plt.ylabel("Deposit")
plt.show()

df["housing"].value_counts()

sns.countplot(x="housing",data=df,hue="marital")
plt.show()

df["contact"].value_counts()

sns.countplot(x="contact",data=df,hue="education")
plt.show()

sns.histplot(data=df, y="day",color="green")
plt.show()

sns.countplot(x="month",data=df,hue="loan",palette="Set2")
plt.show()

sns.histplot(data=df, x="duration",color="crimson",hue="housing",kde=True)
plt.show()

sns.histplot(data=df, x="pdays",color="navy",hue="marital",kde=True)
plt.show()

df["poutcome"].value_counts()

sns.countplot(x="poutcome",data=df,hue="contact")
plt.show()

df["deposit"].value_counts()

sns.countplot(x="deposit",data=df)
plt.show()

cat_data=["job","marital","education","default","housing","loan","contact","month","poutcome"]
from sklearn.preprocessing import LabelEncoder
cat_data = ["job", "marital", "education", "default", "housing", "loan", "contact", "month", "poutcome"]

l = LabelEncoder()

for column in cat_data:
    df[column] = l.fit_transform(df[column])
df["deposit"]=df["deposit"].replace({"yes":1,"no":0})

col=["age","balance","day","month","duration","pdays"]
from sklearn.preprocessing import StandardScaler
sc=StandardScaler()

df[col]=sc.fit_transform(df[col])

X=df.drop(columns="deposit",axis=1)
y=df["deposit"]

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score,confusion_matrix, classification_report, roc_auc_score, roc_curve

model= DecisionTreeClassifier()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)\

cf=confusion_matrix(y_test,y_pred)
sns.heatmap(cf,annot=True,fmt="d",cmap="hsv")
plt.title('Confusion Matrix')
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.show()

print(classification_report(y_test,y_pred))

roc_auc = roc_auc_score(y_test,y_pred)
print("ROC AUC Score:", roc_auc)

import scikitplot as skplt

y_probas = model.predict_proba(X_test)
skplt.metrics.plot_roc(y_test, y_probas)
plt.show()


