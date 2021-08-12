############### COMPUTATIONAL BACK END OF THE PROGRAM
import pandas
import os


def run_reconciliatory():

    global reconciled_list, data_not_in_source #Makes both variables global so then are accessible
                                               #by the reconcile_saveAs and ben_not_in_source_saveAs functions



    file_data_source = open(file_source.name)

    #---- Builds file object of the file data source (i.e, initiated/sent transactions)


    file_data_ben = open(file_ben.name)
    #---- Builds file object of the beneficiaries amount received with beneficiary name


    pandas_df_source = pandas.read_csv(file_data_source)
    #---- Builds pandas Data Frame of the csv file of file_data_source


    pandas_df_ben = pandas.read_csv(file_data_ben)
    #---- Builds pandas Data Frame of the csv file of file_data_ben


    reconciled_list = pandas.DataFrame(columns=["Type", "Time", "IDs", "Order ID", "Text", "From", "To",
                                                "Merchant", "Amount", "Amount with Fee", "Mentioned Amount",
                                                "Status", "", "Beneficiary Name", "Beneficiary Amount"]) #Stores Reconciled/Non-Reconciled Records as list type
    a = 0 # Increment that allows for proper records to be appended to reconciled_list

    test_pandas = pandas_df_source.T #Performs a TRANSPOSE of pandas_df_source


    ## Code segment that creates a list variable and puts Beneficiary amount and name (as list) into it
    ## making a list of lists
    lis_of_ben = []
    for i,j in zip(pandas_df_ben.Amount, pandas_df_ben.Name):
        lis_of_ben.append([i,j])   

        

    ## Function that checks if the amount source exist in the $lis_of_ben variable by looping through $lis_of_ben,
    ## If exists, the function removes the list with Beneficiary name and amount from $lis_of_ben
    ## And then returns through variables: val and ret to the function
    def ben_func(val):
        global c,ret
        #c = 0
        ret = ""
        for i in lis_of_ben:
            if val in i:
                ret = i[1]
                lis_of_ben.remove(i)
                break;

        return val,ret
        
    lis_of_ben_first_checkpoint = list(pandas_df_ben.Amount) # creates list of Amount row in Beneficiary


    for amount_source in pandas_df_source.Amount:
        ttp = test_pandas[a]

        if amount_source in lis_of_ben_first_checkpoint:
            execute_ben_func = ben_func(amount_source) # Executes the ben_func function
            
            ## Creates each row under the columns in reconciled_list DataFrame
            ## if amount source is found in $lis_of_ben_first_checkpoint
            reconciled_list.loc[a] = [ttp[0], ttp[1], ttp[2], ttp[3], ttp[4], ttp[5],
                                      ttp[6], ttp[7], ttp[8], ttp[9], ttp[10],
                                      ttp[11], "", execute_ben_func[1], execute_ben_func[0]]
            
            lis_of_ben_first_checkpoint.remove(amount_source) # removes amount_source from
            #$lis_of_ben_first_checkpoint if $amount_source found in $lis_of_ben_first_checkpoint
            a += 1


                        
        elif amount_source not in lis_of_ben_first_checkpoint:
            ## Creates each row under the columns in reconciled_list DataFrame
            ## if amount source is NOT found in $lis_of_ben_first_checkpoint
            reconciled_list.loc[a] = [ttp[0], ttp[1], ttp[2], ttp[3], ttp[4], ttp[5],
                                      ttp[6], ttp[7], ttp[8], ttp[9], ttp[10],
                                      ttp[11], "", "NOT RECONCILED", ""]
            a += 1
            
            

            # The following pairs were found in Source Data and not Beneficiary Data and Hence, were not RECONCILED
            # The following pairs were found in Beneficiary Data and not in Source Data and Hence, were not RECONCILED

    # Code segment to handle the pairs that were found in Beneficiary Data and not in Source Data
    ##### NOTE: Code segment found in Source Data and not Beneficiary Data are the ones listed with "NOT RECONCILED" in the drake.csv

    data_not_in_source = pandas.DataFrame(columns = ["Beneficiary Name", "Beneficiary Amount"],
                                          data = lis_of_ben)

    
    
    Button_write_reconciled_list = Button(text = "Click to Save\nReconciled Data", command = reconcile_saveAs)
    Button_write_reconciled_list.place(x = 400, y = 350)

    Button_write_data_not_in_source = Button(text = "Click to Save\nBeneficiary Pairs not found in Source",
                                             command = ben_not_in_source_saveAs)
    Button_write_data_not_in_source.place(x = 400, y = 425)

    
        
    print(os.getcwd())

    
def reconcile_saveAs():
    # create filedialog object to save $reconciled_list
    write_reconciled_list = filedialog.asksaveasfile(initialdir="/", defaultextension = "*.csv",
                                                     filetypes = [("Comma Seperated Values", "*.csv")]) 
    reconciled_list.to_csv(write_reconciled_list.name) # Save $reconciled_list to specified .csv file
    label_confirm_save_recon = Label(text = "----- Saved")
    label_confirm_save_recon.place(x = 550, y = 350)
    
    
def ben_not_in_source_saveAs():
    # create filedialog object to save $data_not_in_source
    write_data_not_in_source = filedialog.asksaveasfile(initialdir = "/", defaultextension = "*.csv",
                                                        filetypes = [("Comma Seperated Values", "*.csv")]) 

    data_not_in_source.to_csv(write_data_not_in_source.name) # Save $data_not_in_source to specified .csv file

    label_confirm_ben_pair = Label(text = "----- Saved")
    label_confirm_ben_pair.place(x = 625, y = 425)









########## GUI (FRONT-END) OF THE PROGRAM


from tkinter import *
from tkinter import ttk
from tkinter import font
from tkinter import filedialog



reconApp = Tk()

### create window specifications
width_of_screen = reconApp.winfo_screenwidth()
height_of_screen = reconApp.winfo_screenheight()


## command for Source File Button
def command_source_button():
    global file_source # Makes file_source global and hence, visible by $run_reconiliatory
    try:
        file_source = filedialog.askopenfile(initialdir = "/", filetypes = [("Comma Seperated Values (.csv)", "*.csv")])
        

        ## widget for >>>>>> label
        Label2_Source = Label(text = ">>>>>", font = ("Arial", 22))
        Label2_Source.place(x = 225, y = 189, height = 51, anchor = "nw")


        ### Widget for entry Box in Source
        entry_Source = Entry(reconApp)
        entry_Source.place(x = 337, y = 189, height = 51, width = 250)
        entry_Source.insert(0, file_source.name)
        entry_Source.config(state = DISABLED)

    except AttributeError:
        Label3_Source = Label(text = "You Have Not Selected A File",
                              font = ("Arial", 12, "bold"), fg="red")
        Label3_Source.place(x=337, y = 189, height = 51, width = 250)
        


## command for Beneficiary File Button
def command_ben_button():
    global file_ben # Makes file_ben global and hence, visible by $run_reconiliatory
    try:
        file_ben = filedialog.askopenfile(initialdir = "/", filetypes = [("Comma Seperated Values (.csv)", "*.csv")])
        

        ## widget for >>>>>> label
        Label2_Ben = Label(text = ">>>>>", font = ("Arial", 22))
        Label2_Ben.place(x = 225, y = 275, height = 51, anchor = "nw")


        ### Widget for entry Box in Source
        entry_Ben = Entry(reconApp)
        entry_Ben.place(x = 337, y = 275, height = 51, width = 250)
        entry_Ben.insert(0, file_ben.name)
        entry_Ben.config(state = DISABLED)

    except AttributeError:
        Label3_Ben = Label(text = "You Have Not Selected A File",
                           font = ("Arial", 12, "bold"), fg="red")
        Label3_Ben.place(x = 337, y = 275, height = 51, width = 250)

reconApp.geometry(f"700x500+{int(width_of_screen/4)}+{int(height_of_screen/5)}")

selectedFont1 = font.Font(name = 'font_1', family = 'Segoe UI', size = 21, weight = 'bold', slant = 'roman', underline = 0, overstrike = 0)

## Frame to host both Source and Beneficiary Files
Frame1 = Frame(borderwidth = 3, highlightbackground = '#c0c0c0', relief = 'raised', takefocus = True, )
Frame1.place(x = 769, y = 550, height = 387, width = 770, anchor = 'se')

## Label at top of window
Label_Title = Label(background = '#59dae8', borderwidth = 9, font = 'font_1',
                    image = '', takefocus = True, text = 'Welcome To The Reconciliatory', underline = 1, )
Label_Title.place(x = 137, y = 12, height = 115, width = 469, anchor = 'nw')


## Button to browse to the Source File
Button_Source = Button(background = '#c0c0c0', font = 'TkDefaultFont', image = '',
                takefocus = True, text = 'Click Here to\nBrowse to the Data File',
                 command = command_source_button)
Button_Source.place(x = 17, y = 189, height = 51, width = 192, anchor = 'nw')


## Button to browse to the Beneficiary file
Button_Ben = Button(background = '#c0c0c0', font = 'TkDefaultFont', image = '',
                takefocus = True, text = 'Click Here to\nBrowse the Beneficiary File',
                 command = command_ben_button)
Button_Ben.place(x = 17, y = 275, height = 54, width = 192, anchor = 'nw')


### Reconciliatory Button to run reconciliation
Button_Reconcile = Button(text = "Commence Data Reconciliation", relief = "ridge",
                          font = ("Comic", 10, "bold", "italic"), command = run_reconciliatory)
Button_Reconcile.place(x = 100, y = 350)





reconApp.mainloop()





