# Automata_ICO_Template

************************************************************************ ICO TEMPLATE . PY ************************************************************************
This is the main driver file which uses all other operations for the standard/proper execution of the ICO template
******************************************************************************************************************************************************************* 

Globals:

NEP5_METHODS (contains all the NEP-5 methods in a list)

FUCTIONS IN THIS file:

=> Deploy ( Deploy the initial amount of token => These are to be deployed by the owner of the SC)

Fuction calls in this file:

Note: All these calls are made from the main function (Which can call all the NEP-5 fucntions as well as the following operations)

=> Circulation (Activates the get_circulation () in token.py)
=> mintTokens (Calls the perform_exchange() in crowdsale.py
=> crowdsale_register (Calls the KYC_register() in crowdsale.py)
=> crowdsale_status (Calls the KYC_register() in crowdsale.py)
=> crowdsale_avaiable (Calls the crowdsale_available_amount() in token.py)
=> get_attachements (Calls the get_asset_attachments() in txio.py)

************************************************************************ CrowdSale . PY   ************************************************************************

=> KYC_register (This is a 'Know Your Customer' function and it is used to register people in crowdsale)
=> KYC_status (This is a 'know YOUR CUSTOMER' fucntion and it is used to check the whether you are registered or not)
=> perform_exchange (This function performs the actuall exchange of NEO/GAS to tokens and returns Whether the exchange was successful)
**** yeh iskay under attay hain ****
-> Can_exchange (Determines if the contract invocation meets all requirements for the ICO exchange of neo or gas into NEP5 Tokens
		 and reutrn Whether an invocation meets requirements for exchange after executing the following functions)
-> get_kyc_status (This function returns KYC Status of address provided)
-> calculate_can_exchange (This function returns Whether or not an address can exchange a specified amount by performing some standard checks provided by the Template)

************************************************************************   token . PY    ************************************************************************

Globals:

TOKEN_NAME (Name of the token)
TOKEN_SYMBOL (Symbol of the token)
TOKEN_DECIMALS (Number of decimals the token can contain)
TOKEN_OWNER (Byte array of the owner wallet address) 
TOKEN_CIRC_KEY (This is the key to be put in the database in concatination with the numnber of tokens that are being circulated in the blockchain) 
TOKEN_TOTAL_SUPPLY  (This is total number of the tokens to be distributed in the ICO)
TOKEN_INITIAL_AMOUNT (This contains the amount that the owners are going to keep in their account before the ICO sale)
TOKENS_PER_NEO  (This defines how many tokens are we going to give away for one NEO)
TOKENS_PER_GAS (This defines how many tokens are we going to give away for one GAS)
MAX_EXCHANGE_LIMITED_ROUND (This defines the maximum amount you can mint in the limited round)
BLOCK_SALE_START (This defines the block number from such point in time you want to start the sale)
LIMITED_ROUND_END (This defines the block number from such point in time you want to stop the sale of a limited ICO sale round)
KYC_KEY (This key is put in the database in concatination with some address so that we can determine whether the specific address has been whitelisted or not)0
LIMITED_ROUND_KEY (This key is put in the database in concatination with some address so that we can determine 
		   whether some specific address has already participated in limited sale or not)

Functions:

=> crowdsale_available_amount (This returns The amount of tokens left for sale in the crowdsale)
=> add_to_circulation (This adds an amount of tokens to circlulation)
=> get_circulation (This is used to get the total amount of tokens in circulation)


************************************************************************    NEP 5. PY     ************************************************************************
* I guess there is no need to describe these functions; I've a separate video series for that :D ;) )

Fuctions: 

=> name
=> decimals
=> symbol
=> totalSupply
=> balanceOf
=> transfer
=> transferFrom
=> approve
=> allowance

************************************************************************   txio . PY     ************************************************************************
Globals:

neo_asset_id (This stores the asset ID of NEO)
gas_asset_id (This stores the asset ID of GAS)

Functions:

=> get_asset_attachments (This function gets information about NEO and Gas attached to an invocation TX and returns a list with information about attached neo and gas)
