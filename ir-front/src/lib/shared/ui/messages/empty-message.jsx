//@Dev
// # Shared
// ## Utils
import { cn } from "@/shared/utils/tailwind-merge/tailwind-merge";

export function EmptyMessage({ className, customMessage }) {
  //* @Initiate
  let message = "There is no data";

  if (customMessage) message = customMessage;

  return (
    <p
      className={cn(
        "text-black text-base font-normal capitalize dark:text-white",
        className
      )}
    >
      {message}
    </p>
  );
}
