class BankAccount {
    constructor(owner, balance = 0) {
      this.owner = owner;
      this._balance = balance; 
    }
  
    // Getter method to get the balance
    get balance() {
      return this._balance;
    }
  
    // Setter method to set the balance
    set balance(amount) {
      if (amount >= 0) {
        this._balance = amount;
      } else {
        console.log('Balance cannot be negative.');
      }
    }
  
    // Method to deposit money into the account
    deposit(amount) {
      if (amount > 0) {
        this._balance += amount;
        console.log(`${amount} deposited. New balance: ${this._balance}`);
      } else {
        console.log('Deposit amount must be greater than zero.');
      }
    }
  
    // Method to withdraw money from the account
    withdraw(amount) {
      if (amount > 0 && this._balance >= amount) {
        this._balance -= amount;
        console.log(`${amount} withdrawn. New balance: ${this._balance}`);
      } else if (amount > this._balance) {
        console.log('Insufficient funds.');
      } else {
        console.log('Withdrawal amount must be greater than zero.');
      }
    }
  }
  
  // Create a new bank account
  const account = new BankAccount('John Doe', 1000);
  console.log(account)
  
  // Use setter to change the balance
  account.owner = 'Vidhi'
  account.balance = 500;
  
  // Use getter to access the balance
  console.log(account.owner)
  console.log(account.balance); // Output: 500
  
  // Deposit and withdraw money
  account.deposit(200); // Output: 200 deposited. New balance: 700
  account.withdraw(300); // Output: 300 withdrawn. New balance: 400
  
  // Trying to set a negative balance
  account.balance = -100; // Output: Balance cannot be negative.
  console.log(account._balance)