import streamlit as st
from PIL import Image
from online import st123




st.set_page_config(layout="wide")

st.sidebar.title("Navigation")
page = st.sidebar.selectbox("Select a Page", ["Home", "Notebooks", "Projects"])

st.title("Portfolio")

if page == "Home":
   


    def load_css():
        with open("style.css") as f:
            st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)
        st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

    def st_button(icon, url, label, iconsize):
        if icon == 'youtube':
            button_code = f'''
            <p>
                <a href={url} class="btn btn-outline-primary btn-lg btn-block" type="button" aria-pressed="true">
                    <svg xmlns="http://www.w3.org/2000/svg" width={iconsize} height={iconsize} fill="currentColor" class="bi bi-youtube" viewBox="0 0 16 16">
                        <path d="M8.051 1.999h.089c.822.003 4.987.033 6.11.335a2.01 2.01 0 0 1 1.415 1.42c.101.38.172.883.22 1.402l.01.104.022.26.008.104c.065.914.073 1.77.074 1.957v.075c-.001.194-.01 1.108-.082 2.06l-.008.105-.009.104c-.05.572-.124 1.14-.235 1.558a2.007 2.007 0 0 1-1.415 1.42c-1.16.312-5.569.334-6.18.335h-.142c-.309 0-1.587-.006-2.927-.052l-.17-.006-.087-.004-.171-.007-.171-.007c-1.11-.049-2.167-.128-2.654-.26a2.007 2.007 0 0 1-1.415-1.419c-.111-.417-.185-.986-.235-1.558L.09 9.82l-.008-.104A31.4 31.4 0 0 1 0 7.68v-.123c.002-.215.01-.958.064-1.778l.007-.103.003-.052.008-.104.022-.26.01-.104c.048-.519.119-1.023.22-1.402a2.007 2.007 0 0 1 1.415-1.42c.487-.13 1.544-.21 2.654-.26l.17-.007.172-.006.086-.003.171-.007A99.788 99.788 0 0 1 7.858 2h.193zM6.4 5.209v4.818l4.157-2.408L6.4 5.209z"/>
                    </svg>  
                    {label}
                </a>
            </p>'''

            
        elif icon == 'linkedin':
            button_code = f'''
            <p>
                <a href={url} class="btn btn-outline-primary btn-lg btn-block" type="button" aria-pressed="true">
                    <svg xmlns="http://www.w3.org/2000/svg" width={iconsize} height={iconsize} fill="currentColor" class="bi bi-linkedin" viewBox="0 0 16 16">
                        <path d="M0 1.146C0 .513.526 0 1.175 0h13.65C15.474 0 16 .513 16 1.146v13.708c0 .633-.526 1.146-1.175 1.146H1.175C.526 16 0 15.487 0 14.854V1.146zm4.943 12.248V6.169H2.542v7.225h2.401zm-1.2-8.212c.837 0 1.358-.554 1.358-1.248-.015-.709-.52-1.248-1.342-1.248-.822 0-1.359.54-1.359 1.248 0 .694.521 1.248 1.327 1.248h.016zm4.908 8.212V9.359c0-.216.016-.432.08-.586.173-.431.568-.878 1.232-.878.869 0 1.216.662 1.216 1.634v3.865h2.401V9.25c0-2.22-1.184-3.252-2.764-3.252-1.274 0-1.845.7-2.165 1.193v.025h-.016a5.54 5.54 0 0 1 .016-.025V6.169h-2.4c.03.678 0 7.225 0 7.225h2.4z"/>
                    </svg>
                    {label}
                </a>
            </p>''' 
        elif icon == 'medium':
            button_code = f'''
            <p>
                <a href={url} class="btn btn-outline-primary btn-lg btn-block" type="button" aria-pressed="true">
                    <svg xmlns="http://www.w3.org/2000/svg" width={iconsize} height={iconsize} fill="currentColor" class="bi bi-medium" viewBox="0 0 16 16">
                        <path d="M9.025 8c0 2.485-2.02 4.5-4.513 4.5A4.506 4.506 0 0 1 0 8c0-2.486 2.02-4.5 4.512-4.5A4.506 4.506 0 0 1 9.025 8zm4.95 0c0 2.34-1.01 4.236-2.256 4.236-1.246 0-2.256-1.897-2.256-4.236 0-2.34 1.01-4.236 2.256-4.236 1.246 0 2.256 1.897 2.256 4.236zM16 8c0 2.096-.355 3.795-.794 3.795-.438 0-.793-1.7-.793-3.795 0-2.096.355-3.795.794-3.795.438 0 .793 1.699.793 3.795z"/>
                    </svg>
                    {label}
                </a>
            </p>'''
        
        elif icon == 'cup':
            button_code = f'''
            <p>
                <a href={url} class="btn btn-outline-primary btn-lg btn-block" type="button" aria-pressed="true">
                    <svg xmlns="http://www.w3.org/2000/svg" width={iconsize} height={iconsize} fill="currentColor" class="bi bi-cup-fill" viewBox="0 0 16 16">
                        <path d="M1 2a1 1 0 0 1 1-1h11a1 1 0 0 1 1 1v1h.5A1.5 1.5 0 0 1 16 4.5v7a1.5 1.5 0 0 1-1.5 1.5h-.55a2.5 2.5 0 0 1-2.45 2h-8A2.5 2.5 0 0 1 1 12.5V2zm13 10h.5a.5.5 0 0 0 .5-.5v-7a.5.5 0 0 0-.5-.5H14v8z"/>
                    </svg>
                    {label}
                </a>
            </p>'''
        elif icon == '':
            button_code = f'''
            <p>
                <a href={url} class="btn btn-outline-primary btn-lg btn-block" type="button" aria-pressed="true">
                    {label}
                </a>
            </p>'''
        return st.markdown(button_code, unsafe_allow_html=True)

    load_css()

    col1, col2, col3 = st.columns(3)
    col2.image(Image.open('8bit.png'))

    st.header('Alexander Palmer')

    st.info("About Me: ")
    st.info("Data Science student at UNC Charlotte")

    icon_size = 20

    st_button('youtube', 'https://youtube.com', 'YouTube channel', icon_size)
    st_button('medium', 'https://medium.com/', 'Read my Blogs', icon_size)
    st_button('linkedin', 'https://www.linkedin.com/', 'Follow me on LinkedIn', icon_size)
    st_button('cup', 'https://www.buymeacoffee.com/', 'Buy me a Coffee', icon_size)

elif page == "Notebooks":
    st.header("Notebooks")
    st.write("This is the Notebook page.")
    
    
    query = st.text_area("Enter SQL Query")
    if st.button("Execute"):
        
        st.write("Query executed.")
       
elif page == "Projects": 
    import streamlit as st
   from PIL import Image
   
   st.set_page_config(layout="wide")
   
   st.title(" :blue[Project 1:] ")
   st.title(" :blue[JPX-Tokyo Stock Exchange Data] ")
   
   st.header("Introduce the Problem")
   st.write(
       """
       
       #
       The objective is to use the market data to rank the stocks. To see if theres any relation in volatility and to find if Sharpe ratio is a good ranking ratio.
   
       The biggest winners in the stock market are those who are able to identify solid under valued investments. One notably investor is Carl Icahn. He had a business model that involved taking a large stake in underbought companies he believed to be undervalued. He would make large profits by identifying and buying solid under valued stocks and sale his position after they became overvalued. He was labeled as a successful investor on Wall Street and a hostile activist shareholder because of his investment strategies and takeovers.
   
       In this analysis we will explore quantitative trading where predictions can be made. The financial data includes stock information and historical stock prices that can be analyzed. With over 2,000 stock data points we can analyze returns and movements. This will allow us rank using the Sharpe Ratio.
   
       Lets first start small by analyzing one stock then build from there.
   
       """
   )
   
   st.header("Introduce the Data")
   st.write(
       """
       #
       
       
       The Data-set is from the Kaggle competition: JPX Tokyo Stock Exange Predict. 
       #
       https://www.kaggle.com/competitions/jpx-tokyo-stock-exchange-prediction/data
   
       The competition is described in the above link. 
   
       
   
       The data includes stock_list and different csv files:
   
           financials.csv
           options.csv
           secondary_stocks_prices.csv
           stock_prices.csv
           trads.csv
   
       Lets first load our data and do some manipulation in pandas to prepare it in a readable format.
   
       The Data-set contains quantitive data of 2,000 commonly traded stocks and options in the Japanese stock market. Some of the stock names include KYOKUYO CO, NIKKO EXCHANGE, and FIT Corporation from the years 2017 to 2021. Each security can be identified by a SecuritiesCode
   
       The columns included in the stock_price csv file:
   
       
               .
   
               RowId: Unique ID of price records
               
               Date: Trade date 
               
               SecuritiesCode: Local securities code 
               
               Open: First traded price on a day in JPY
   
               High: Highest traded price on a day in JPY
   
               Low: Lowest traded price on a day in JPY
   
               Close: Last traded price on a day in JPY
   
               Volume: Number of traded stocks on a day 
               
               AdjustmentFactor: Used to calculate price when split
   
               ExpectedDividend: Expected dividend value
   
               Target: Change ratio
   
       #           
   
   
       """
   
   )
   image1 = Image.open("online/img_1.jpg")
   image2 = Image.open("online/img_2.jpg")
   image3 = Image.open("online/img_3.jpg")
   image4 = Image.open("online/img_4.jpg")
   image5 = Image.open("online/img_5.jpg")
   image6 = Image.open("online/img_6.jpg")
   image7 = Image.open("online/img_7.jpg")
   
   st.image(image1, caption=None)
   st.image(image2, caption=None)
   
   st.header("Pre-processing the Data")
   st.write(
       """
       
       
       Lets look find a security code that relates to us:
       
       Mcdonalds is in Japan.
       The security code is 2702. It will be good to convert the price from JPY to USD so we can understand it better.
       
       
       """
   
   )
   
   st.write(
       """
       Lets use cardinality and correlation to elminate unuseful columns and rows
   
           - column RowID is in string format is not useful as SecurityCode. We can get the same information by calling this column.
   
           - column Date is useful since we need this to find the deviation
   
           - Price columns (High, Low, Open and Close) are useful but is in JPX not USD. It is also missing 7608 values. We will need to replace this by comparing it to the Volume column.
   
           - column Volue should have Nan for non trading days such as weekends. The missing values are related to the non trading days and can be replaced with 0 or NaN
   
       When Analyzing the data we should check for the number of NaN values for each column and if the Volume column contains the same number of 0's as the number of missing values in the Close column.
   
       We need to find a way to augment the data and replace values for the empty rows to fill Open, High, Low and Close.
   
       There was also some important things to consider such as the Equity Trading System failure on Oct 1, 2020 and other system failures for missing data
   
       pct_change()
   
       Pandas has a funtion that calculates the percentage of change between elements in a row from the previous row.
   
       Keep in mind volatility represents how large the stock prices swing around the average price. Less volitale means that the price is expected to stay around the average. There are several ways to measure volatility such as option pricing model and standard deviations of returns. 
   
       We also need to know the moving average which is the rolling mean or movin mean. It is the moving average that is used in time-series to capture the short-term swing while keeping up with the trends. The average can measure swings in seconds,minutes, hours and days or any selected time-frame. For our analysis we want to measure days and periods.
   
       
       """
   )
   st.image(image3, caption=None)
   
   st.header("Data Understanding/Visualization")
   st.write(
       """
       We can visualise the data.
       Let's look at Mcdonalds stock and see the percentage of return as well as the closing price each day.
       And lets compare the amount of shares traded so we can see if it relates to the return or closing price.
       """
   )
   st.image(image4, caption=None)
   
   st.header("Storytelling")
   st.write(
       """
       The competition uses the Sharpe Ratio to evaluate and rank the 200 highest stocks.
   
       Sharpe Ratio is used to evaluate the daily spread of returns. Investopedia explains the Sharpe Ratio as a mathematical expression the measures risk and volatility. 
   
       The name comes from Economist William Sharpe in 1966 who called it a reward-to-variability ratio.
   
       The formula and calculation of the Sharpe Ratio:
       Return - Risk Free Rate/Theta
   
       
       """
   
   )
   st.image(image5, caption=None)
   
   st.write(
       """
       We are looking for something that has a small denominator compared to its numerator. This type of analysis is better when comparing stocks to its peers.
   
       The denominator is calculated by:
   
           Take the return variance(How far each number in a data set is from the average) from the average return in each of the incremental periods, square it, and sum the squares from all the incremental periods.
   
           Divide the sum by the number of incremental time periods.
   
           Take a square root of the quotient.
   
       The Sharpe Ratio can tell us the risk-adjusted relative return. It can compare a stocks historical amount relating to its benchmark to the expected variablity of the return. In other words the Sharpe Ratio compares reward to the risk.
   
       If we wanted to find the Sharpe Ratio for Mcdonalds holdings we would first find the average annual return and then compare it to a low-risk investment like a government bond or ETF. We would subtract rate of the bond from Mcdonalds stock rate and then divide it by the Standard Deviation rate of Mcdonalds stock. Sharpe Ratios above 1 are considered "good" and offers excess returns compared to its volatility. However investors usually compare stocks in a portfolio with those in the market sector. So if Mcdonalds is in a ETF it would be compared with stocks in the Consumer Discretionary sector in USA, but this is not the same sector in Japan.
   
       """
   )
   
   st.image(image6, caption=None)
   
   
   st.image(image7, caption=None)
   
   st.header("Impact Section")
   
   st.write(
       """
       A strategy can be used to rank the stock using the Sharpe Ratio and seting a buy vs sell alert. The alert can get triggered if the ratio is above 1.5 and also if the price is below the historical close price.
   
       It will also be beneficial to keep track of trends and entry/exit timing. The trend can measure the current price relatice to the average high and low over the previous periods. The entry/exit measure the stock volume of buying and selling pressure. We can set a indicater to represent if the stock is oversold or overbought.
           
       """
   )
   
   st.write(
       """
       Sharpe Ratio is good formula but considers movement in either direction risky. In other words the Sharpe ratio creates a curve that the stock should follow and gives it a score or rank based off the closeness to that curve. Even if the price is above the curve then the rank can be skewed. Risk is assessed only off a deviation of the standard. It treats positive and negitive returns equally. Another fact about the Sharpe Ratio is uses a linear relationship meaning it expects the return to be equally impacted by the price. In reality investors consider the upside potential when buying stocks and other securites. Investors will buy volitile stocks with the potential of higher returns. An investor may ignore the ratio and sell, just so they can cut their loses. There are other variations of the Sharpe Ratio called Sortino Ratio that ignores the above-average returns and focus on the downside deviation to handle risk.
   
       """
   )
   
   st.header("References")
   st.write(
       """
       https://www.investopedia.com/terms/s/sharperatio.asp
   
       https://www.kaggle.com/competitions/jpx-tokyo-stock-exchange-prediction/overview
   
       https://medium.com/codex/algorithmic-trading-with-relative-strength-index-in-python-d969cf22dd85
   
       https://www.investopedia.com/terms/m/macd.asp
   
       https://www.educba.com/moving-average-formula/
   
       https://www.alphacodingskills.com/pandas/notes/pandas-function-dataframe-pct-change.php
   
       https://www.kaggle.com/code/onurkoc83/technical-features-trading-strategy
   
       https://www.kaggle.com/code/ikeppyo/examples-of-higher-scores-than-perfect-predictions
       
       """
   )
   st.header("Code")
   
   
   
   
   
