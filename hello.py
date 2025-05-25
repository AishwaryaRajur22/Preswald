import plotly.express as px

from preswald import (
    get_df,
    plotly,
    text,
)

# Report Title
text(
    "# Mall Customer Data Analysis \n This report explores customer demographics, income, and spending behavior."
)

# Load the CSV
df = get_df("malldata_csv")


# 1. Scatter plot 
text(
    "## Income vs. Spending Score \n Relationship between annual income and spending score, grouped by gender."
)
fig1 = px.scatter(
    df,
    x="Annual_Income($)",
    y="Spending_Score",
    color="Gender",
    title="Income vs. Spending Score by Gender",
    labels={"Annual_Income($)": "Income(k$)", "Spending_Score": "Spending Score(1-100)"},
    hover_data=["Age"]
)
fig1.update_layout(template="plotly_white")
plotly(fig1)

# 2. Histogram of Sepal Length
text(
    "## Spending Score Distribution \n Frequency of spending scores, segmented by gender."
)
fig2 = px.histogram(
    df, 
    x="Spending_Score", 
    color="Gender",
    title="Spending Score Distribution by Gender",
    labels={"Spending_Score": "Spending Score (1-100)"},
    opacity=0.7,
)
fig2.update_layout(template="plotly_white")
plotly(fig2)

# 3. Box Plot: Age Distribution by Gender 
text("## Age Distribution by Gender \n Spread of customer ages across genders.")
fig3 = px.box(
    df,
    x="Gender",  
    y="Age",
    color="Gender",
    title="Age Distribution by Gender",
    labels={"Age": "Age (years)"}
)
fig3.update_layout(template="plotly_white")
plotly(fig3)
