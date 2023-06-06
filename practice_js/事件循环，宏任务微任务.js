setTimeout(function () {
  console.log(1);
});
new Promise((resolve) => {
  console.log(2);
  new Promise(() => {
    console.log(3);
  });
  resolve();
}).then((_) => {
  console.log(4);
});
console.log(5);
