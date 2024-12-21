# Automated Market Maker (AMM)
This project simulates a basic Automated Market Maker (AMM) system for exchanging fruit assets, such as Apples and Oranges. It demonstrates how liquidity pools work, how exchange rates are determined using the constant product formula, and how assets can be traded in a decentralized finance (DeFi) model. The system allows for managing initial assets, liquidity pools, and performing fruit exchanges based on available liquidity.

## Known Issues

- **Large Volume Exchange**: 
  When exchanging very large quantities of one asset (e.g., millions of Apples), the exchange rate may be significantly impacted due to slippage. This can cause the amount of the buy asset received to be much lower than expected. The current implementation does not prevent such large trades, and the effect of slippage is not properly constrained for large transactions.

-  **Example**: 
   If you try to exchange 50,000,000 Apples for Oranges in the liquidity pool, the price impact could be severe due to limited liquidity. As a result, you may receive far fewer Oranges than expected, even if the initial quantity of Oranges is high (e.g., 50,000,000 Oranges).


