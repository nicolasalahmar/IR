//@Dev
// # Shared
// ## Utils
import { cn } from "@/shared/utils/tailwind-merge/tailwind-merge";

export function ErrorMessage({ className, error }) {
  //* @Initiate
  let message = "unexpected error occurred";

  if (error.server) message = error.message;

  return (
    <p className={cn("text-error text-base font-normal capitalize", className)}>
      {message}
    </p>
  );
}
