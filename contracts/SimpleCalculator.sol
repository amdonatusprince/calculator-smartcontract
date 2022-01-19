// SPDX-License-Identifier: MIT

pragma solidity ^0.6.0;

contract SimpleCalculator{
    // Declaring state variable  
    // uint result;

    function add(uint[] memory numberArray) public pure returns(uint){
    uint i;
    uint sum = 0;
    for(i = 0; i < numberArray.length; i++)
        sum = sum + numberArray[i];
    return sum;
  }
    function subtract(uint num1, uint num2) public returns (uint){
        uint result = num1 - num2;
        return result;
  }
    function multiply(uint num1, uint num2) public returns(uint) {
        uint result = num1 * num2;
    return result;
  }
  function divide(uint num1, uint num2) public returns (uint){
    uint result = num1 / num2;
    return result;
  }

}