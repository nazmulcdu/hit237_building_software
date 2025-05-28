function toggleSection(header) {
    const next = header.nextElementSibling;
    const isHidden = next.classList.contains('hidden');

    // Toggle visibility
    next.classList.toggle('hidden');

    // Toggle arrow direction
    if (isHidden) {
        header.innerHTML = header.innerHTML.replace('⬇️', '⬆️');
    } else {
        header.innerHTML = header.innerHTML.replace('⬆️', '⬇️');
    }
}
