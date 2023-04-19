import csv
import pandas as pd
import time

# def createFsnPlaCsv(fsn_ids: str = ""):
#     pla_fsn = fsn_ids.split(",")
#     print(pla_fsn)

#     df = pd.read_csv("addFsnPla/pla_fsn.csv")
#     index = list(range(1, df.shape[0]))
#     df.drop(index, axis=0, inplace=True)
#     df.to_csv("addFsnPla/pla_fsn.csv", index=False)
#     print(df)

#     df1 = pd.DataFrame(pla_fsn)
#     df1.to_csv("addFsnPla/pla_fsn.csv", mode="a", index=False, header=False)


# createFsnPlaCsv(fsn_ids="a,b,d")


# with open('addFsnPla/pla_fsn.csv', 'w', encoding="ISO-8859-1", newline='') as myfile:
#     wr = csv.writer(myfile)
#     wr.writerow(pla_fsn)
# myfile.close()

# df = pd.DataFrame({"exact":['a','b','c','d'], "broad":['','','','']})
# print(df)


def createFsnPlaCsv(exact_keyword: str = "", broad_keyword: str = ""):
    exact_pla_keyword = exact_keyword.split(",")
    print(exact_pla_keyword)
    broad_pla_keyword = broad_keyword.split(",")
    print(broad_pla_keyword)
    # broad_pla_keyword =[]
    # len_exact = len(exact_pla_keyword)
    # for i in range(0,len_exact):
    #     broad_pla_keyword.append('')

    print(broad_pla_keyword)

    # to remove the rows
    df = pd.read_csv("addKeywordPla/pla_keyword.csv")
    print(df)
    df.drop(df.filter(regex="Unname"), axis=1, inplace=True)
    # df.loc[:, ~df.columns.str.match('Unnamed')]
    print(df)

    print("a", df.shape)
    print("b", df.shape[0])
    index = list(range(1, df.shape[0]))
    print("index", index)
    df.drop(index, axis=0, inplace=True)
    # df.to_csv("addKeywordPla/pla_keyword.csv", index=False,)
    print(df)
    time.sleep(3)

    # df1 = pd.DataFrame.from_dict({'Broad': broad_pla_keyword, 'Exact': exact_pla_keyword}, orient='index').T
    # print(df1)
    # df1.to_csv("addKeywordPla/pla_keyword.csv", mode="a", index=False, header=False)
    # time.sleep(3)


createFsnPlaCsv(exact_keyword="a,b,e,e", broad_keyword="z")
