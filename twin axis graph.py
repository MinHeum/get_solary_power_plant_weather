## twin axis graph
fig, ax1 = plt.subplots(figsize=(12, 8), dpi=150)

color1 = '색상'
ax1.set_xlabel('date')
ax1.set_ylabel('close price', color=color1)  
ax1.plot(dat['date'], dat['열1'])
ax1.tick_params(axis='y', labelcolor=color1)

ax2 = ax1.twinx()  # 두 번째 축

color2 = '색상'
ax2.set_ylabel('volume', color=color2)  
ax2.plot(dat['date'], dat['열2'])
ax2.tick_params(axis='y', labelcolor=color2)

ax1.set_title('제목', loc='left', fontsize=15)
plt.show()