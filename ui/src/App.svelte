<script>
	let records = [
		{ done: false, text: 'finish Svelte tutorial' },
		{ done: false, text: 'build an app' },
		{ done: false, text: 'world domination' }
	];

    let username = "";
    let password = "";
    let yes = false

    function handleSubmit() {
        // send AJAX request to django backend.
        console.log("Credentials:", username, password, yes);
        username = "";
        password = "";
    }

    function addCard() {
        // POST card
        console.log("adding card...");
    }

</script>

<h1>Cardbase UI Testing Environment</h1>

<form on:submit|preventDefault={handleSubmit}>
    <input placeholder="Username..." bind:value={username}>
    <input placeholder="Password..." bind:value={password}>
    <label>
        <input type=checkbox bind:checked={yes}>
        Remember my username.
    </label>
    <button>Log In</button>
</form>


<h1>Current Active Cards</h1>

{#each records as record}
    <p>{record.text}</p>
{/each}

<h2>Actions</h2>
<button on:click={addCard}>Add Card</button>
