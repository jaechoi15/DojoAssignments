// Write a function that will make it print like:
// 0 -> James
// 1 -> Jill
// 2 -> Jane
// 3 -> Jack

function fancyArray(arr)
{
    var arr = ["James", "Jill", "Jane", "Jack"];

    for (var i = 0; i < arr.length; i++)
    {
        console.log(i + " -> " + arr[i]);
    }
}
fancyArray();