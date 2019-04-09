import matplotlib.pyplot as plt

labels = 'here', 'you', 'go'
f = [12, 34, 56]

def pieChart():
    fig, axs = plt.subplots(2, 2)
    patches, texts, autotexts = axs[0, 0].pie(f, labels=labels,
                                              autopct='%.0f%%',
                                              textprops={'size': 'smaller'},
                                              shadow=False, radius=0.5,
                                              explode=(0.05, 0, 0))

    patches, texts, autotexts = axs[0, 1].pie(f, labels=labels,
                                              autopct='%.0f%%',
                                              textprops={'size': 'smaller'},
                                              shadow=False, radius=0.5,
                                              explode=(0.05, 0, 0))
    patches, texts, autotexts = axs[1, 0].pie(f, labels=labels,
                                              autopct='%.0f%%',
                                              textprops={'size': 'smaller'},
                                              shadow=False, radius=0.5,
                                              explode=(0.05, 0, 0))

    patches, texts, autotexts = axs[1, 1].pie(f, labels=labels,
                                              autopct='%.0f%%',
                                              textprops={'size': 'smaller'},
                                              shadow=False, radius=0.5,
                                              explode=(0.05, 0, 0))
    plt.setp(autotexts, size='x-small')
    autotexts[0].set_color('white')
    
    plt.show()
