// async function getEntries() {
//     const url = '/api/entries'
//     let result = await fetch(url,{
//             method: 'GET',
//             headers: {
//                 'Content-Type': 'application/json',
//                 'x-access-token': `Bearer ${'b738a5058cb01722dad257fcc9ea660c547443e5a2a065a3'}`
//             }
//         });
//     console.log(result)
//     if (!response.ok){
//         console.log('Failed to fetch data from server')
//     }
//     let response = await result.json();
//     console.log(response);
// }

// getEntries()