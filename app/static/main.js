async function getEntries() {
    const url = 'https://api.goprogram.ai/inspiration'
    let result = await fetch(url,{
            method: 'GET'
        });
    let response = await result.json();

    var dailyInspiration = [response.quote, response.author]

    console.log(dailyInspiration)

    let div = document.getElementById('inspiration')

    //add quote
    let quote = document.createElement("h3")
    quote.textContent = dailyInspiration[0]
    div.appendChild(quote)

    //add author
    let author = document.createElement('h5')
    author.textContent = '-- ' + dailyInspiration[1]
    author.classList.add('text-end')
    div.appendChild(author)
}

getEntries()