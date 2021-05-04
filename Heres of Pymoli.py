import pandas as pd
import numpy as np

file_to_load = "Resources/purchase_data.csv"
pur_data = pd.read_csv(file_to_load)

total_players = len(pur_data["SN"].value_counts())

player_count = pd.DataFrame({"Total Players":[total_players]})

player_count

number_of_unique_items = len((pur_data["Item ID"]).unique())
average_price = (pur_data["Price"]).mean()
number_of_purchases = (pur_data["Purchase ID"]).count()
total_revenue = (pur_data["Price"]).sum()

summary_df = pd.DataFrame({"Number of Unique Items":[number_of_unique_items],
                           "Average Price":[average_price], 
                           "Number of Purchases": [number_of_purchases], 
                           "Total Revenue": [total_revenue]})

summary_df.style.format({'Average Price':"${:,.2f}",
                         'Total Revenue': '${:,.2f}'})
summary_df

gender_stats = pur_data.groupby("Gender")

total_count_gender = gender_stats.nunique()["SN"]
 
percentage_of_players = total_count_gender / total_players * 100

gender_demos = pd.DataFrame({"Percentage of Players": percentage_of_players, "Total Count": total_count_gender})

gender_demo.index.name = None

gender_demo.sort_values(["Total Count"], ascending = False).style.format({"Percentage of Players":"{:.2f}"})

pur_count = gender_stats["Purchase ID"].count()

avg_pur_price = gender_stats["Price"].mean()

avg_pur_total = gender_stats["Price"].sum()

avg_pur_capita = avg_purchase_total/total_count_gender

gender_demo = pd.DataFrame({"Purchase Count": pur_count, 
                                    "Average Purchase Price": avg_pur_price,
                                    "Average Purchase Value":avg_pur_total,
                                    "Avg Purchase Total per Person": avg_pur_capita})

gender_demo.style.format({"Average Purchase Value":"${:,.2f}",
                                  "Average Purchase Price":"${:,.2f}",
                                  "Avg Purchase Total per Person":"${:,.2f}"})

                                  age_bins = [0, 9, 14, 19, 24, 29, 34, 39, 200]
group_names = ["<10", "10-14", "15-19", "20-24", "25-29", "30-34", "35-39", "40+"]

pur_data["Age Group"] = pd.cut(pur_data["Age"],age_bins, labels=group_names)
pur_data

age_grouped = pur_data.groupby("Age Group")

total_count_age = age_grouped["SN"].nunique()

percentage_by_age = (total_count_age/total_players) * 100

age_demo = pd.DataFrame({"Percentage of Players": percentage_by_age, "Total Count": total_count_age})

age_demo.index.name = None

age_demo.style.format({"Percentage of Players":"{:,.2f}"})

pur_count_age = age_grouped["Purchase ID"].count()
avg_pur_price_age = age_grouped["Price"].mean()
total_pur_value = age_grouped["Price"].sum()
avg_pur_capita_age = total_pur_value/total_count_age

age_demo = pd.DataFrame({"Purchase Count": pur_count_age,
                                 "Average Purchase Price": avg_pur_price_age,
                                 "Total Purchase Value":total_pur_value,
                                 "Average Purchase Total per Person": avg_pur_capita_age})

age_demo.index.name = None

age_demo.style.format({"Average Purchase Price":"${:,.2f}",
                               "Total Purchase Value":"${:,.2f}",
                               "Average Purchase Total per Person":"${:,.2f}"})

                               spender_stats = pur_data.groupby("SN")
pur_count_spender = spender_stats["Purchase ID"].count()
avg_pur_price_spender = spender_stats["Price"].mean()
pur_total_spender = spender_stats["Price"].sum()

top_spend = pd.DataFrame({"Purchase Count": pur_count_spender,
                             "Average Purchase Price": avg_pur_price_spender,
                             "Total Purchase Value":pur_total_spender})

clean_spend = top_spend.sort_values(["Total Purchase Value"], ascending=False).head()

clean_spend.style.format({"Average Purchase Total":"${:,.2f}",
                            "Average Purchase Price":"${:,.2f}", 
                            "Total Purchase Value":"${:,.2f}"})

                            items = pur_data[["Item ID", "Item Name", "Price"]]
item_stats = items.groupby(["Item ID","Item Name"])
pur_count_item = item_stats["Price"].count() 
pur_value = (item_stats["Price"].sum()) 
item_price = pur_value/pur_count_item

most_popular_items = pd.DataFrame({"Purchase Count": pur_count_item, 
                                   "Item Price": item_price,
                                   "Total Purchase Value":pur_value})

popular_formatted = most_popular_items.sort_values(["Purchase Count"], ascending=False).head()

popular_formatted.style.format({"Item Price":"${:,.2f}",
                                "Total Purchase Value":"${:,.2f}"})

                                popular_formatted = most_popular_items.sort_values(["Total Purchase Value"],
                                                   ascending=False).head()
popular_formatted.style.format({"Item Price":"${:,.2f}",
                                "Total Purchase Value":"${:,.2f}"})