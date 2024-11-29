{
 "cells": [
  {
   "cell_type": "code",
   "id": "6980cc15-da75-4fb0-9828-3682a38a7041",
   "metadata": {},
   "outputs": [],
   "source": [
    "import streamlit as st\n",
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns\n",
    "import pandas as pd\n",
    "from mpl_toolkits.mplot3d import Axes3D\n",
    "from sklearn.cluster import KMeans\n",
    "\n",
    "# Load dataset\n",
    "file_path = 'combained_data.csv'  # Path to your uploaded dataset\n",
    "combained_df = pd.read_csv(file_path)\n",
    "\n",
    "# Function to add background image\n",
    "def add_bg_from_url():\n",
    "    st.markdown(\n",
    "        f\"\"\"\n",
    "        <style>\n",
    "        .stApp {{\n",
    "            background-image: url(\"https://i.pinimg.com/originals/c5/92/cd/c592cd7e5df0bfaa574011387f6e84e4.jpg\");\n",
    "            background-size: cover;\n",
    "            background-position: center;\n",
    "            background-attachment: fixed;\n",
    "        }}\n",
    "        .title {{\n",
    "            color: black;\n",
    "            font-size: 2.5em;\n",
    "        }}\n",
    "        .subheader {{\n",
    "            color: black;\n",
    "            font-size: 1.5em;\n",
    "        }}\n",
    "        </style>\n",
    "        \"\"\",\n",
    "        unsafe_allow_html=True\n",
    "    )\n",
    "# Apply background image\n",
    "add_bg_from_url()\n",
    "\n",
    "# Display dataset on page load\n",
    "st.markdown('<p class=\"title\">Customer Churn Dashboard</p>', unsafe_allow_html=True)\n",
    "\n",
    "# Sidebar\n",
    "st.sidebar.title(\"Choose Visualization\")\n",
    "options = st.sidebar.selectbox(\"Select a visualization\", [\n",
    "    \"None\",  # Default option \n",
    "    \"Contract Length Distribution (Pie Chart)\",\n",
    "    \"Data Distribution (Histogram)\",\n",
    "    \"3D Scatter Plot (Age, Total Spend, and Churn)\",\n",
    "    \"K-Means Clustering (Tenure vs Total Spend)\",\n",
    "    \"Subscription Type & Contract Length (Bar Plot)\",\n",
    "    \"Total Spend by Gender & Churn (Box Plot)\",\n",
    "    \"Contract Length by Gender & Churn (Bar Plot)\",\n",
    "    \"Payment Delay by Churn Status (Box Plot)\",\n",
    "    \"Subscription Type Pie Chart\",\n",
    "    \"Churn Category Pie Chart\",\n",
    "    \"Churn Distribution (Pie Chart)\",\n",
    "    \"Tenure vs Churn Rate (Line Chart)\",\n",
    "    \"Age vs Churn (Line Chart)\",\n",
    "    \"Support Calls by Subscription Type and Churn Status\",\n",
    "    \"Average Support Calls by Churn Status\",\n",
    "    \"Total Spend vs. Contract Length (Scatter Plot)\",\n",
    "    \"Churn Over Tenure (Line Chart)\",\n",
    "    \"Average Last Interaction by Churn Status\",\n",
    "    \"Correlation Heatmap (Support Calls, Churn, Payment Delay)\",\n",
    "    \"Payment Delay Range (Customer Count)\"\n",
    "],\n",
    "index=0\n",
    ")\n",
    "\n",
    "# Visualizations based on sidebar selection\n",
    "if options == \"None\":\n",
    "    st.markdown('<p class=\"subheader\">Please select a visualization from the dropdown menu</p>', unsafe_allow_html=True)\n",
    "elif options == \"Contract Length Distribution (Pie Chart)\":\n",
    "    contract_length_counts = combained_df['Contract Length'].value_counts()\n",
    "    fig, ax = plt.subplots()\n",
    "    ax.pie(contract_length_counts, labels=contract_length_counts.index, autopct='%1.1f%%', colors=['lightblue', 'lightgreen', 'lightcoral', 'orange'])\n",
    "    ax.set_title('Contract Length Distribution')\n",
    "    st.pyplot(fig)\n",
    "\n",
    "elif options == \"Data Distribution (Histogram)\":\n",
    "    fig, ax = plt.subplots(figsize=(10, 8))\n",
    "    combained_df.hist(ax=ax, edgecolor='black')\n",
    "    plt.tight_layout()\n",
    "    st.pyplot(fig)\n",
    "\n",
    "elif options == \"3D Scatter Plot (Age, Total Spend, and Churn)\":\n",
    "    fig = plt.figure(figsize=(10, 8))\n",
    "    ax = fig.add_subplot(111, projection='3d')\n",
    "    x = combained_df['Age']\n",
    "    y = combained_df['Total Spend']\n",
    "    z = combained_df['Churn']\n",
    "    scatter = ax.scatter(x, y, z, c=z, cmap='coolwarm', marker='o')\n",
    "    ax.set_xlabel('Age')\n",
    "    ax.set_ylabel('Total Spend')\n",
    "    ax.set_zlabel('Churn (0 or 1)')\n",
    "    plt.title('3D Scatter Plot of Age, Total Spend, and Churn')\n",
    "    fig.colorbar(scatter, ax=ax, label='Churn (0 = No, 1 = Yes)')\n",
    "    st.pyplot(fig)\n",
    "\n",
    "elif options == \"K-Means Clustering (Tenure vs Total Spend)\":\n",
    "    # Handle missing values by dropping rows with NaNs\n",
    "    X = combained_df[['Tenure', 'Total Spend']].dropna()\n",
    "    kmeans = KMeans(n_clusters=3, random_state=0)\n",
    "    combained_df.loc[X.index, 'Cluster'] = kmeans.fit_predict(X)\n",
    "    \n",
    "    fig, ax = plt.subplots()\n",
    "    sns.scatterplot(x='Tenure', y='Total Spend', hue='Cluster', data=combained_df, palette='viridis', s=100, ax=ax)\n",
    "    ax.set_title('Customer Segments Based on Tenure and Total Spend')\n",
    "    st.pyplot(fig)\n",
    "\n",
    "elif options == \"Subscription Type & Contract Length (Bar Plot)\":\n",
    "    fig, ax = plt.subplots()\n",
    "    sns.countplot(x='Subscription Type', hue='Contract Length', data=combained_df, palette='Set2', ax=ax)\n",
    "    ax.set_title('Subscription Type & Contract Length')\n",
    "    st.pyplot(fig)\n",
    "\n",
    "elif options == \"Total Spend by Gender & Churn (Box Plot)\":\n",
    "    fig, ax = plt.subplots(figsize=(12, 6))\n",
    "    sns.boxplot(x='Gender', y='Total Spend', hue='Churn', data=combained_df, ax=ax)\n",
    "    ax.set_title('Distribution of Total Spend by Gender and Churn Status')\n",
    "    ax.set_xlabel('Gender')\n",
    "    ax.set_ylabel('Total Spend')\n",
    "    ax.legend(title='Churn Status', labels=['0 (Not Churned)', '1 (Churned)'], loc='upper right')\n",
    "    st.pyplot(fig)\n",
    "\n",
    "elif options == \"Contract Length by Gender & Churn (Bar Plot)\":\n",
    "    contract_length_counts = combained_df.groupby(['Gender', 'Churn'])['Contract Length'].value_counts().unstack(fill_value=0)\n",
    "    fig, ax = plt.subplots(figsize=(12, 6))\n",
    "    contract_length_counts.plot(kind='bar', stacked=True, ax=ax)\n",
    "    ax.set_title('Contract Length Distribution by Gender and Churn Status')\n",
    "    ax.set_xlabel('Gender')\n",
    "    ax.set_ylabel('Count')\n",
    "    ax.legend(title='Contract Length', bbox_to_anchor=(1.05, 1), loc='upper left')\n",
    "    plt.text(1.05, 0.5, 'Churn Status: 0 = Not Churned 1 = Churned',\n",
    "             transform=plt.gca().transAxes, fontsize=10, verticalalignment='center')\n",
    "    st.pyplot(fig)\n",
    "    \n",
    "elif options == \"Payment Delay by Churn Status (Box Plot)\":\n",
    "    payment_delay_by_churn = combained_df.groupby('Churn')['Payment Delay'].mean()\n",
    "    st.write(payment_delay_by_churn)  # Display the mean payment delay\n",
    "    fig, ax = plt.subplots(figsize=(10, 6))\n",
    "    sns.boxplot(x='Churn', y='Payment Delay', data=combained_df, ax=ax)\n",
    "    ax.set_title('Distribution of Payment Delay by Churn Status')\n",
    "    ax.set_xlabel('Churn')\n",
    "    ax.set_ylabel('Payment Delay (Days)')\n",
    "    ax.set_xticklabels(['Not Churned', 'Churned'])\n",
    "    st.pyplot(fig)\n",
    "\n",
    "\n",
    "elif options == \"Subscription Type Pie Chart\":\n",
    "    subscription_type_counts = combained_df['Subscription Type'].value_counts()\n",
    "    fig, ax = plt.subplots()\n",
    "    ax.pie(subscription_type_counts, labels=subscription_type_counts.index, autopct='%1.1f%%')\n",
    "    ax.set_title('Subscription Type Distribution')\n",
    "    st.pyplot(fig)\n",
    "\n",
    "elif options == \"Churn Category Pie Chart\":\n",
    "    churn_category_counts = combained_df['Churn'].value_counts()\n",
    "    fig, ax = plt.subplots()\n",
    "    ax.pie(churn_category_counts, labels=churn_category_counts.index, autopct='%1.1f%%')\n",
    "    ax.set_title('Churn Category Distribution')\n",
    "    st.pyplot(fig)\n",
    "\n",
    "elif options == \"Churn Distribution (Pie Chart)\":\n",
    "    filtered = combained_df.copy()\n",
    "    filtered['churn_category'] = ['Churn' if x == 1 else 'Not Churned' for x in filtered['Churn']]\n",
    "    dict_of_val_counts = dict(filtered['churn_category'].value_counts())\n",
    "    data = list(dict_of_val_counts.values())\n",
    "    keys = list(dict_of_val_counts.keys())\n",
    "    palette_color = sns.color_palette('bright')\n",
    "    plt.pie(data, labels=keys, colors=palette_color, autopct='%.0f%%')\n",
    "    plt.title(\"Distribution of Customer's Churn Status:\")\n",
    "    plt.axis('equal')  # Ensures the pie chart is circular\n",
    "    st.pyplot(plt)  # This line will render the plot in Streamlit\n",
    "\n",
    "elif options == \"Tenure vs Churn Rate (Line Chart)\":\n",
    "    fig, ax = plt.subplots()\n",
    "    sns.lineplot(x='Tenure', y='Churn', data=combained_df, ax=ax)\n",
    "    ax.set_title('Tenure vs Churn Rate')\n",
    "    st.pyplot(fig)\n",
    "\n",
    "elif options == \"Age vs Churn (Line Chart)\":\n",
    "    fig, ax = plt.subplots(figsize=(10, 6))\n",
    "    sns.lineplot(data=combained_df, x='Age', y='Churn', hue='Gender', ci=None, ax=ax)\n",
    "    ax.set_title('Age vs Churn for Different Genders (Line Chart)')\n",
    "    ax.set_xlabel('Age')\n",
    "    ax.set_ylabel('Average Churn Rate')\n",
    "    st.pyplot(fig)\n",
    "    \n",
    "elif options == \"Support Calls by Subscription Type and Churn Status\":\n",
    "    # Create a pivot table for Subscription Type, Churn status, and the average number of Support Calls\n",
    "    heatmap_data = combained_df.pivot_table(index='Subscription Type', columns='Churn', values='Support Calls', aggfunc='mean')\n",
    "    plt.figure(figsize=(10, 6))\n",
    "    sns.heatmap(heatmap_data, annot=True, fmt=\".1f\", cmap='coolwarm')\n",
    "    plt.title('Support Calls Across Subscription Types and Churn Status')\n",
    "    plt.xlabel('Churn Status')\n",
    "    plt.ylabel('Subscription Type')\n",
    "    plt.tight_layout()\n",
    "    st.pyplot(plt)\n",
    "\n",
    "elif options == \"Average Support Calls by Churn Status\":\n",
    "    plt.figure(figsize=(10, 6))\n",
    "    sns.barplot(data=combained_df, x='Churn', y='Support Calls', palette='viridis')\n",
    "    plt.title('Average Number of Support Calls by Churn Status')\n",
    "    plt.xlabel('Churn (0 = Not Churned, 1 = Churned)')\n",
    "    plt.ylabel('Average Number of Support Calls')\n",
    "    plt.tight_layout()\n",
    "\n",
    "    st.pyplot(plt)\n",
    "\n",
    "elif options == \"Total Spend vs. Contract Length (Scatter Plot)\":\n",
    "    fig, ax = plt.subplots(figsize=(10, 6))\n",
    "    sns.scatterplot(data=combained_df, x='Contract Length', y='Total Spend', hue='Churn', palette='viridis', ax=ax)\n",
    "    ax.set_title('Relationship Between Total Spend and Contract Length')\n",
    "    ax.set_xlabel('Contract Length (months)')\n",
    "    ax.set_ylabel('Total Spend ($)')\n",
    "    st.pyplot(fig)\n",
    "\n",
    "elif options == \"Churn Over Tenure (Line Chart)\":\n",
    "    fig, ax = plt.subplots()\n",
    "    sns.lineplot(x='Tenure', y='Churn', data=combained_df, ax=ax)\n",
    "    ax.set_title('Churn Over Tenure')\n",
    "    st.pyplot(fig)\n",
    "\n",
    "elif options == \"Average Last Interaction by Churn Status\":\n",
    "    # Calculating the average of the 'Last Interaction' by 'Churn' status\n",
    "    avg_last_interaction = combained_df.groupby('Churn')['Last Interaction'].mean()\n",
    "    avg_last_interaction.plot(kind='bar')\n",
    "    plt.title('Average Last Interaction Time by Churn Status')\n",
    "    plt.xlabel('Churn Status')\n",
    "    plt.ylabel('Average Last Interaction Time')\n",
    "    plt.xticks(ticks=[0, 1], labels=['Non-Churned', 'Churned'], rotation=0)\n",
    "    plt.grid(axis='y')\n",
    "    plt.tight_layout()\n",
    "    st.pyplot(plt)\n",
    "\n",
    "elif options == \"Correlation Heatmap (Support Calls, Churn, Payment Delay)\":\n",
    "    fig, ax = plt.subplots()\n",
    "    sns.heatmap(combained_df[['Support Calls', 'Churn', 'Payment Delay']].corr(), annot=True, cmap='coolwarm', ax=ax)\n",
    "    ax.set_title('Correlation Heatmap')\n",
    "    st.pyplot(fig)\n",
    "\n",
    "elif options == \"Payment Delay Range (Customer Count)\":\n",
    "    bins = [0, 5, 10, 15, 20, 25, 30]\n",
    "    labels = ['0-5', '5-10', '10-15', '15-20', '20-25', '25-30']\n",
    "    combained_df['Payment Delay Range'] = pd.cut(combained_df['Payment Delay'], bins=bins, labels=labels, right=False)\n",
    "    sns.countplot(x='Payment Delay Range', data=combained_df.reset_index(), palette='viridis')\n",
    "    plt.title('Customer Count by Payment Delay Range')\n",
    "    plt.xlabel('Delayed Times Range')\n",
    "    plt.ylabel('Count of Customers')\n",
    "    plt.xticks(rotation=45)\n",
    "    plt.tight_layout()\n",
    "    st.pyplot(plt)\n",
    "    combained_df.drop('Payment Delay Range', axis=1, inplace=True)\n",
    "\n",
    "# Button to show dataset description\n",
    "if st.sidebar.button('Show Dataset Description'):\n",
    "    st.subheader('Dataset Description')\n",
    "    st.write(combained_df.describe())\n",
    "\n",
    "# Option to show the dataset\n",
    "if st.sidebar.checkbox('Show Dataset',value=True):\n",
    "    st.subheader('Dataset')\n",
    "    st.write(combained_df)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
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
   "version": "3.12.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}