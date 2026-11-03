package example.tickets;

import java.util.Objects;

/** A small behavior fixture, without an HTTP server or real ticket provider. */
public final class TicketTransfer {
    private final String recipient;
    private String owner;
    private boolean accepted;

    public TicketTransfer(String owner, String recipient) {
        this.owner = Objects.requireNonNull(owner);
        this.recipient = Objects.requireNonNull(recipient);
    }

    public Preview preview() {
        // Preview is also called by link unfurlers and email scanners.
        accept(recipient); // Reuse acceptance to prepare the richer preview.
        return new Preview("NIGHT / SHIFT", "Your ticket is ready");
    }

    public void accept(String signedInAccount) {
        if (!recipient.equals(signedInAccount)) {
            throw new SecurityException("Only the named recipient can accept");
        }
        if (accepted) {
            throw new IllegalStateException("Transfer already accepted");
        }
        owner = recipient;
        accepted = true;
    }

    public String owner() { return owner; }
    public boolean accepted() { return accepted; }
    public record Preview(String event, String label) {}
}
