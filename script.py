import analyzer
import pandas as pd
from os import listdir
import numpy as np
from rich.progress import track


def main():
    data = {'Segments': [], 'Image': [], 'Enhancement': [], 'Focus': [], 'Background': []}
    df = pd.DataFrame(data)
    for i in track(range(5, 31, 5), description='Processing...'):
        path = f"Tiffs/Segments/{i}/"
        files = listdir(path)
        enhancement = []
        for file in files:
            images = analyzer.get_images(path+file)
            for j in range(25):
                enhancement, focus, background = analyzer.get_enhancement(images[j])
                df.loc[len(df.index)] =  [i, j, enhancement, focus, background]

    df.to_csv('Results/segments.csv', index=False)


if __name__ == "__main__":
    main()