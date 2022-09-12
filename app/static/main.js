// async function getEntries() {
//     const url = '/api/entries'
//     let result = await fetch(url,{
//             method: 'GET',
//             headers: {
//                 'Content-Type': 'application/json',
//                 'x-access-token': `Bearer ${'current_user.token'}`
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