import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Data for demographic table
demographic_data = {
    "Pseudonym": ["P1", "P2", "P3", "P4", "P5", "P6", "P7"],
    "Gender": ["Male", "Female", "Male", "Male", "Male", "Male", "Male"],
    "Industry": ["Software Development"] * 7
}

# Creating DataFrame for demographic table
demographic_df = pd.DataFrame(demographic_data)

# Data for thematic analysis table
thematic_data = {
    "Theme": [
        "Engagement", "Engagement", "Contributions", "Contributions", 
        "Tools", "Tools", "Perceptions", "Perceptions", 
        "Group Formation", "Group Formation", "Meeting Dynamics", "Meeting Dynamics"
    ],
    "Sub-theme": [
        "Active Participation", "Passive Listening", "Equal Contribution", "Unequal Contribution", 
        "Effective Tools", "Integration Challenges", "Positive View of Remote Work", "Negative View of Remote Work", 
        "Social Group Formation", "No Group Formation", "Increased Collaboration On-site", "Collaboration Possible Remotely"
    ],
    "Description": [
        "On-site participants show more active participation compared to remote participants",
        "Remote participants often engage in passive listening",
        "Some feel remote participants contribute equally",
        "Most feel remote participants contribute less",
        "Microsoft Teams and external microphones are found effective",
        "Difficulty in integrating some tools into the hybrid meeting environment",
        "Remote work is seen as convenient by some participants",
        "Others feel remote work reduces engagement and effectiveness",
        "Co-located employees tend to form social groups, leading to exclusion of remote workers",
        "Some do not perceive significant group formation",
        "Face-to-face meetings lead to better collaboration",
        "Collaboration can be effective remotely with the right tools and practices"
    ],
    "Count of Participants": [5, 4, 2, 5, 6, 3, 3, 4, 5, 2, 5, 3]
}

# Creating DataFrame for thematic analysis table
thematic_df = pd.DataFrame(thematic_data)

# Data for challenges identified
challenges_data = {
    "Challenges Identified": [
        "Technical Issues", "Distraction and Zoning Out", "Lack of Social Interaction", 
        "Engagement Issues", "Biases", "Group Formation"
    ],
    "Description": [
        "Problems with microphones and other technical infrastructure",
        "Participants feel more distracted and zone out during remote meetings",
        "Missing informal chit-chat and social interaction present in on-site meetings",
        "Remote participants often less engaged and proactive",
        "Perceived biases where on-site participants see remote ones as less engaged or committed",
        "Formation of social groups among on-site participants leading to exclusion of remote workers"
    ],
    "Count of Participants": [4, 3, 4, 5, 3, 5]
}

# Creating DataFrame for challenges identified
challenges_df = pd.DataFrame(challenges_data)

# Data for suggestions for improvement
suggestions_data = {
    "Suggestions for Improvement": [
        "Improved Technical Infrastructure", "Regular On-site Meetings", 
        "Better Meeting Practices", "Enhanced Collaboration Tools", 
        "Clear Communication Guidelines"
    ],
    "Description": [
        "Use of better microphones and cameras for clearer communication",
        "Having regular on-site meetings to complement hybrid and remote meetings",
        "Implementing better practices for engaging remote participants",
        "Using advanced collaboration tools to bridge the gap between on-site and remote participants",
        "Establishing clear guidelines for communication to ensure inclusivity and engagement"
    ],
    "Count of Participants": [5, 4, 3, 4, 4]
}

# Creating DataFrame for suggestions for improvement
suggestions_df = pd.DataFrame(suggestions_data)

# Define color palette for descriptions
color_palette = {
    "On-site participants show more active participation compared to remote participants": "#1f77b4",
    "Remote participants often engage in passive listening": "#ff7f0e",
    "Some feel remote participants contribute equally": "#2ca02c",
    "Most feel remote participants contribute less": "#d62728", 
    "Microsoft Teams and external microphones are found effective": "#9467bd", 
    "Difficulty in integrating some tools into the hybrid meeting environment": "#8c564b", 
    "Remote work is seen as convenient by some participants": "#e377c2", 
    "Others feel remote work reduces engagement and effectiveness": "#7f7f7f", 
    "Co-located employees tend to form social groups, leading to exclusion of remote workers": "#bcbd22", 
    "Some do not perceive significant group formation": "#17becf", 
    "Face-to-face meetings lead to better collaboration": "#aec7e8", 
    "Collaboration can be effective remotely with the right tools and practices": "#ffbb78",
    "Problems with microphones and other technical infrastructure": "#1f77b4",
    "Participants feel more distracted and zone out during remote meetings": "#ff7f0e",
    "Missing informal chit-chat and social interaction present in on-site meetings": "#2ca02c",
    "Remote participants often less engaged and proactive": "#d62728",
    "Perceived biases where on-site participants see remote ones as less engaged or committed": "#9467bd",
    "Formation of social groups among on-site participants leading to exclusion of remote workers": "#8c564b",
    "Use of better microphones and cameras for clearer communication": "#1f77b4",
    "Having regular on-site meetings to complement hybrid and remote meetings": "#ff7f0e",
    "Implementing better practices for engaging remote participants": "#2ca02c",
    "Using advanced collaboration tools to bridge the gap between on-site and remote participants": "#d62728",
    "Establishing clear guidelines for communication to ensure inclusivity and engagement": "#9467bd"
}

# Function to create custom legends
def create_custom_legend(ax, data, title, use_theme=True):
    from matplotlib.lines import Line2D

    handles = []
    labels = []
    
    if use_theme:
        for theme, group in data.groupby('Theme'):
            labels.append(theme)
            handles.append(Line2D([0], [0], color='w', markerfacecolor='w', markersize=0))
            for desc in group['Description'].unique():
                color = color_palette[desc]
                handles.append(Line2D([0], [0], color=color, lw=6))
                labels.append(f'  {desc}')
    else:
        for desc in data['Description'].unique():
            color = color_palette[desc]
            handles.append(Line2D([0], [0], color=color, lw=6))
            labels.append(desc)
    
    ax.legend(handles, labels, loc='upper left', bbox_to_anchor=(1,1), title=title)

# Sort thematic_df by Theme and Description to match the legend order
thematic_df = thematic_df.sort_values(by=["Theme", "Description"])

# Convert the color palette to a list for consistent coloring
colors = [color_palette[desc] for desc in thematic_df['Description']]

# Bar Chart for Thematic Analysis (Grouped) using Seaborn
plt.figure(figsize=(14, 10))
ax1 = sns.barplot(data=thematic_df, x='Theme', y='Count of Participants', hue='Description', palette=color_palette, dodge=True, width=0.6)
plt.title('What do participants feel about Hybrid Meetings', fontsize=14)
plt.xlabel('Major Themes', fontsize=12)
plt.ylabel('Count of Participants', fontsize=12)
plt.yticks(range(0, int(thematic_df['Count of Participants'].max()) + 2, 1))
plt.xticks(rotation=45, ha='right')
create_custom_legend(ax1, thematic_df, 'Description')
plt.tight_layout()
plt.show()

# Pie Chart for Challenges Identified
plt.figure(figsize=(10, 10))
challenge_colors = [color_palette[desc] for desc in challenges_df['Description']]
challenges_df.set_index('Challenges Identified')['Count of Participants'].plot(kind='pie', autopct='%1.1f%%', colors=challenge_colors)
plt.title('Challenges Identified in Hybrid Meetings', fontsize=14)
plt.ylabel('')
plt.tight_layout()
plt.show()

plt.figure(figsize=(14, 10))
suggestions_grouped = suggestions_df.groupby(['Suggestions for Improvement', 'Description'])['Count of Participants'].sum().unstack().fillna(0)
suggestions_colors = [color_palette[desc] for desc in suggestions_grouped.columns]
ax2 = suggestions_grouped.plot(kind='barh', stacked=True, color=suggestions_colors, figsize=(14, 10))
plt.title('Suggestions for Improvement in Hybrid Meetings', fontsize=14)
plt.xlabel('Count of Participants', fontsize=12)
plt.ylabel('Suggestions for Improvement', fontsize=12)
plt.xticks(range(0, int(suggestions_grouped.values.max().sum()) + 2, 1))
plt.xlim(0, int(suggestions_grouped.values.max().sum()) + 1)
create_custom_legend(ax2, suggestions_df, 'Description', use_theme=False)
plt.tight_layout()
plt.show()